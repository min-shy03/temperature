from flask import Blueprint, render_template, request, jsonify
from app.models import ClassMember
from .. import db
import random

bp = Blueprint('cleaning', __name__, url_prefix='/cleaning')

@bp.route('/')
def show() :
    grade = request.args.get('grade', default=1, type=int)

    unchecked_list_unsorted = ClassMember.query.filter_by(grade=grade, check=False).all()
    checked_list_unsorted = ClassMember.query.filter_by(grade=grade, check=True).all()
    this_week_member_list_unsorted = ClassMember.query.filter_by(grade=grade, this_week=True).all()

    unchecked_list = sorted(unchecked_list_unsorted, key=lambda member : member.name)
    checked_list = sorted(checked_list_unsorted, key=lambda member : member.name)
    this_week_member_list = sorted(this_week_member_list_unsorted, key=lambda member : member.name)

    return render_template(
        'cleaning_page.html', 
        grade=grade, 
        unchecked_list=unchecked_list,
        checked_list=checked_list,
        this_week_member_list=this_week_member_list
    )

@bp.route('/api/add-member', methods=['POST'])
def add_member() :
    data = request.json

    grade = data.get('grade')
    name = data.get('name')
    gender = data.get('gender')
    position = data.get('position')
    
    if not all([grade, name, gender, position]) :
        return jsonify({'success' : False, 'message' : '모든 필드를 입력해야 합니다.'}), 400
    
    existing_member = ClassMember.query.filter_by(grade=grade, name=name).first()

    if existing_member :
        return jsonify({'success': False, 'message': f'{grade}학년에 이미 \'{name}\' 학생이 존재합니다.'}), 409

    try :
        member = ClassMember(grade=grade, name=name, gender=gender, position=position)
        db.session.add(member)
        db.session.commit()
        return jsonify({'success': True, 'message': '저장 완료'}), 200

    except Exception as e :
        db.session.rollback()
        print(f"API Update 오류: {e}")
        return jsonify({'success':False, 'message': f'DB 저장 실패 : {e}'}), 500
    
@bp.route('/api/grade-members', methods=['GET'])
def get_members_by_grade() :
    grade = request.args.get('grade')

    if not grade :
        return jsonify({"success" : False, "message" : "학년이 필요합니다."}), 400
    
    member_unsorted = ClassMember.query.filter_by(grade=grade).all()
    members = sorted(member_unsorted, key=lambda m: m.name)

    student_list = []
    for s in members :
        student_list.append({
            "id" : s.id,
            "name" : s.name,
            "position" : s.position,
            "gender" : s.gender
        })

    return jsonify(student_list)

@bp.route('/api/member/<int:student_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_mamber(student_id) :
    member = ClassMember.query.get_or_404(student_id)

    if request.method == 'GET' :
        return jsonify({
            "success" : True,
            "id" : member.id,
            "name" : member.name,
            "gender" : member.gender,
            "position" : member.position    
        })
    
    elif request.method == 'PUT' :
        data = request.json
        
        member.gender = data.get('gender')
        member.position = data.get('position')

        try :
            db.session.commit()
            return jsonify({"success" : True, "message" : "학생 정보가 수정되었습니다."})
        except Exception as e :
            db.session.rollback()
            return jsonify({"success" : False, "message" : f"수정 실패 {str(e)}"}), 500
    
    elif request.method == 'DELETE' :
        try :
            db.session.delete(member)
            db.session.commit()
            return jsonify({"success" : True, "message" : "학생이 삭제되었습니다."})
        except Exception as e :
            db.session.rollback()
            return jsonify({"success" : False, "message" : f"삭제 실패 {str(e)}"}), 500
        
@bp.route('/api/draw', methods=['POST'])
def draw():
    grade = request.args.get('grade')
    all_members = ClassMember.query.filter_by(grade=grade).all()
    
    # [수정] 쿼리문으로 강제 업데이트하지 않고, 객체를 하나씩 '직접' 초기화합니다.
    # 이렇게 해야 나중에 다시 True로 바꿨을 때 파이썬이 "변경사항 있음!"으로 인식해서 저장합니다.
    for m in all_members:
        m.this_week = False 

    # 1. 후보 확인 (check가 False인 사람)
    candidates = [m for m in all_members if not m.check]
    this_week_list = []

    # ---------------------------------------------------------
    # [핵심] 후보가 4명 안 되면? -> 리셋해서 강제로 채움
    # ---------------------------------------------------------
    if len(candidates) < 4:
        # 1단계: 남은 후보는 일단 다 당번 시킴
        this_week_list.extend(candidates)
        
        # 2단계: 몇 명 더 필요한지 계산
        needed = 4 - len(this_week_list)
        
        # 3단계: 전체 리셋! (모두를 다시 후보 상태로 만듦)
        for m in all_members:
            m.check = False
        
        # 4단계: 방금 뽑힌 애들(this_week_list) 뺀 나머지 중에서 부족분 채우기
        pool = [m for m in all_members if m not in this_week_list]
        
        # 인원이 충분하면 랜덤 추출, 부족하면 전원 투입
        if len(pool) >= needed:
            extras = random.sample(pool, needed)
            this_week_list.extend(extras)
        else:
            this_week_list.extend(pool)

    # ---------------------------------------------------------
    # [일반] 후보가 4명 이상이면? -> 그냥 4명 뽑음
    # ---------------------------------------------------------
    else:
        this_week_list = random.sample(candidates, 4)

    # 2. 결과 확정 (이번에 뽑힌 4명 처리)
    for m in this_week_list:
        m.this_week = True  # 화면에 '이번 주 당번' 표시
        m.check = True      # '한 사람' 목록으로 이동

    try:
        db.session.commit()
        
        # 요청하신 메시지 형식 100% 유지
        new_member_list = sorted([member.name for member in this_week_list])
        
        return jsonify({
            'success': True, 
            'message': "청소 당번을 새로 뽑았습니다.", 
            'new_members': new_member_list
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': f'DB 저장 오류 {str(e)}'}), 500

# 학년 교체 API
@bp.route('api/promote', methods=['POST'])
def promote() :
    try :
        # 3학년
        graduates = ClassMember.query.filter_by(grade=3).all()
        # 3학년은 정보 삭제
        if graduates :
            for member in graduates :
                db.session.delete(member)

        # 2학년
        seniors = ClassMember.query.filter_by(grade=2).all()
        if seniors :
            for member in seniors :
                member.grade = 3
        # 1학년
        juniors = ClassMember.query.filter_by(grade=1).all()
        if juniors :
            for member in juniors :
                member.grade = 2

        db.session.commit()

        return jsonify({'success' : True, 'message' : "학년을 교체했습니다."}), 200
    except Exception as e :
        db.session.rollback()
        return jsonify({'success' : False, 'message' : f"학년 교체 중 오류 발생 {str(e)}"}), 500
    
@bp.route('api/init', methods=['POST'])
def init() :
    grade = request.args.get('grade')

    try : 
        member_list = ClassMember.query.filter_by(grade=grade).all()

        if member_list :
            for member in member_list :
                member.check = False
                member.this_week = False

            db.session.commit()

            return jsonify({'success' : True, 'message' : "청소 당번을 초기화 했습니다."}), 200
    
    except Exception as e :
        db.session.rollback()
        return jsonify({'success' : False, 'message' : f"당번 초기화 중 오류 발생 {str(e)}"}),500
