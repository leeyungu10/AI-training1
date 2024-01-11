import kss
from konlpy.tag import Komoran

def foreigner_style_korean(input_text):
    komoran = Komoran()
    sentences = kss.split_sentences(input_text)

    foreigner_style_text = ""

    for sentence in sentences:
        tokens = komoran.pos(sentence)

        for token, pos in tokens:
            # 외국인 스타일 처리 로직 추가 예시
            if pos.startswith('N'):  # 명사
                # 외국인 스타일에 맞게 명사를 다른 단어로 대체
                token = "foreign_noun"
            
            foreigner_style_text += token + " "

    return foreigner_style_text.strip()

# 테스트
user_input = input("한국어를 입력하세요: ")
output_text = foreigner_style_korean(user_input)
print("외국인 스타일 한국어:", output_text)