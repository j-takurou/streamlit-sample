import streamlit as st
from transformers import BertTokenizer, BertModel
import torch


def highlight(word, attn):
    # アテンションの値に応じて色の濃さを調整
    html_color = '#%02X%02X%02X' % (255, int(255*(1 - attn)), int(255*(1 - attn)))
    return '<span style="background-color: {}"> {}</span>'.format(html_color, word)


st.title('BERT アテンション可視化アプリ')

text_input = st.text_area("テキストを入力してください")

if text_input:
    # ここでBERTモデルとトークナイザをロード
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased', output_attentions=True)

    # ここでアテンションを取得
    inputs = tokenizer(text_input, return_tensors='pt')
    outputs = model(**inputs)
    attentions = outputs.attentions

    # アテンションの平均を計算
    avg_attention = torch.mean(attentions[-1], dim=1)  # 最後のレイヤーのアテンションを平均
    avg_attention = avg_attention.squeeze(0)

    # HTMLの生成
    html = ""
    for token, attn in zip(inputs['input_ids'][0], avg_attention):
        word = tokenizer.decode([token])
        html += highlight(word, attn.item())

    # StreamlitでHTMLを表示
    st.markdown(html, unsafe_allow_html=True)
