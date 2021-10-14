import streamlit as st

st.title("DOD・Nierシリーズ年表")
st.subheader('DOD　Nierシリーズとは…')
st.write("## ・DOD")
st.write("## 「ドラッグ オン ドラグーン シリーズ」（英: DRAG-ON DRAGOON series）は、スクウェア・エニックスから発売されているアクションロールプレイングゲームシリーズである。また、鬱ゲーである")
st.subheader('・Nier')
'''
 『NieR』シリーズとは、スクウェア・エニックスが発売しているゲームプロジェクト。略称は「NieR」または「ニーア」。鬱ゲーム の傑作として名高い『ドラッグオンドラグーン』を手掛けたチームによる開発ということで注目を集めた。DODと同じく癖の強い設定こそ多いものの、作風は王道となっており、ユーザー間の評価も高い。
'''

option = st.selectbox('## どの作品が知りたい？',('DOD','DOD2','DOD3','Nier Replicant','Nier Gestalt','Nier Automata'))

if option=='DOD':
    st.write('異世界ミッドガルドを舞台に、亡国の王子カイムとレッドドラゴンが縦横無尽に駆け巡る勧善懲悪の冒険活劇。')