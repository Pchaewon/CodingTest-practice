import os
import csv
from post import Post
# 파일 경로
file_path = "./myvenv/Chapter12/data.csv"

# post객체를 저장할 리스트
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf-8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
        #print(data)
    #pass
else:
    # 파일 생성하기
    f = open(file_path, "w", encoding="utf-8", newline="")
    f.close()

# # post_list 테스트
# print(post_list)
# print(post_list[0].get_title())

# 게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""
    print("\n********게시글 쓰기*********")
    title = input("제목을 입력해주세요\n>>>")
    content = input("내용을 입력해 주세요\n>>>")
    #글번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

# 게시글 목록
def list_post():
    """게시글 목록 함수"""    
    #print(post_list)
    print("\n * 게시글 목록")
    id_list = []
    for post in post_list:
        print("번호 :", post.get_id())
        print("제목 :", post.get_title())
        print("조회수 :", post.get_view_count())
        print("")
        id_list.append(post.get_id())
        
    while True:
        print("Q) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력해주세요)")
        try:
            id = int(input(">>>"))
            if id in id_list:
                #print("게시글 상세보기")
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("없는 글 번호입니다.")
        except ValueError:
            print("숫자를 입력해 주세요")
        
# 글 상세 페이지
def detail_post(id):
    """ 게시글 상세 보기 함수 """
    print("\n * 게시글 상세")
    
    for post in post_list:
        if post.get_id() == id:
            # 조회수 1 증가
            post.add_view_count()
            print("번호 :", post.get_id())        
            print("제목 :", post.get_title())        
            print("본문 :", post.get_content())        
            print("조회수 :", post.get_view_count())        
            targetpost = post
            
    while True:
        print("Q) 수정: 1 삭제: 2 (메뉴로 돌아가려면 -1을 입력)")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                update_post(targetpost)
                break
                #print("수정")
            elif choice == 2:
                delete_post(targetpost)
                #print("삭제")
                break
            elif choice == -1:
                break
            else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해 주세요")

# 게시글 수정
def update_post(target_post):
    """게시글 수정 함수"""
    print("\n 게시글 수정")
    title = input("제목을 수정해 주세요.")
    content = input("본문을 입력해 주세요.")
    target_post.set_post(target_post.id, title, content, target_post.view_count)
    print("# 게시글이 수정되었습니다.")

# 게시글 삭제
def delete_post(target_post):
    """게시글 삭제 함수"""
    post_list.remove(target_post)
    print("# 게시글이 삭제되었습니다.")   

# 게시글 저장
def save():
    """게시글 저장 함수"""
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("# 저장이 완료 되었습니다.")
    print("# 프로그램 종료.")
    
# 메뉴 출력하기
while True:
    print("\n******Chaewon BLOG*****")
    print("**메뉴를 선택해주세요**")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해 주세요")
    else:
        if choice==1:
            write_post()
            #print("게시글 쓰기")
        elif choice==2:
            list_post()
            #print("게시글 목록")
        elif choice==3:
            save()
            #print("프로그램 종료")
            break