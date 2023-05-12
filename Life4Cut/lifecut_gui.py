import tkinter as tk
from tkinter import filedialog
from PIL import Image
import datetime
import random

def process_photos():
    # 템플릿 이미지 경로
    template_path = "/Users/suhancho/Downloads/black/K-BioX.Template.wobox.png"

    # 사진 파일 경로들
    photo_paths = photo_listbox.get(0, tk.END)

    # 템플릿 이미지 로드
    template = Image.open(template_path)

    # 템플릿 이미지 크기 설정 (1115 × 2918)
    template_size = (1115, 2918)
    template = template.resize(template_size)

    # 사진들을 올릴 위치를 정의
    photo_width = 884  # 사진 가로 크기
    photo_height = 580  # 사진 세로 크기
    left_margin = 114  # 좌측 여백
    top_margin = 93  # 상단 여백
    bottom_margin = 336  # 하단 여백
    photo_spacing = 55  # 사진 간 여백
    # 사진 개수에 따라 배치를 다르게 처리
    # 사진 개수에 따라 배치를 다르게 처리
    if len(photo_paths) == 1:
        # 사진이 한 개인 경우, 동일한 사진 4번 추가
        photo_paths *= 4
    elif len(photo_paths) == 2:
        # 사진이 두 개인 경우, 각 사진을 2번 반복
        photo_paths *= 2
    elif len(photo_paths) == 3:
        # 사진이 세 개인 경우, 모두 사용하고 나머지 한 개는 무작위로 추가
        random_photo = random.choice(photo_paths)
        photo_paths.append(random_photo)
    elif len(photo_paths) >= 4:
        # 사진이 네 개 이상인 경우, 첫 번째부터 네 번째까지 모두 사용하고 나머지는 제외
        photo_paths = photo_paths[:4]

    # 사진들을 템플릿 이미지에 배치
    photo_positions = [(left_margin, top_margin),
                       (left_margin, top_margin + photo_height + photo_spacing),
                       (left_margin, top_margin + 2 * (photo_height + photo_spacing)),
                       (left_margin, top_margin + 3 * (photo_height + photo_spacing))]
    for i, photo_path in enumerate(photo_paths):
        photo = Image.open(photo_path)
        photo = photo.resize((photo_width, photo_height))
        template.paste(photo, photo_positions[i])
    # 결과 이미지 저장
    output_filename = output_entry.get()
    if not output_filename:
        # output 파일명이 지정되지 않은 경우, 현재 날짜와 시간으로 파일명 생성
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"lifecut_result_{current_datetime}"
    output_path = f"{output_filename}.jpg"
    template.save(output_path)
    result_label.config(text="프로그램이 성공적으로 실행되었습니다.")

def add_photos():
    # 파일 선택 대화상자 열기
    file_paths = filedialog.askopenfilenames()

    # 선택된 사진 파일들을 리스트박스에 추가
    for file_path in file_paths:
        photo_listbox.insert(tk.END, file_path)

def reset_photos():
    # 선택된 사진 파일들 초기화
    photo_listbox.delete(0, tk.END)
    result_label.config(text="")

# GUI 생성
window = tk.Tk()
window.title("인생네컷 프로그램")
window.geometry("400x400")

# 사진 파일 선택 버튼
add_photos_button = tk.Button(window, text="사진 파일 선택", command=add_photos)
add_photos_button.pack()

# 선택된 사진 파일 목록
photo_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, width=40, height=5)
photo_listbox.pack(pady=10)

# 처리 버튼
# 처리 버튼
process_button = tk.Button(window, text="처리하기", command=process_photos)
process_button.pack()

# Output 파일명 입력
output_label = tk.Label(window, text="Output 파일명:")
output_label.pack()
output_entry = tk.Entry(window)
output_entry.pack()

# 결과 텍스트
result_label = tk.Label(window, text="")
result_label.pack()

# 다시 하기 버튼
reset_button = tk.Button(window, text="다시 하기", command=reset_photos)
reset_button.pack()

window.mainloop()
