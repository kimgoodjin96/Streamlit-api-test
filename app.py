import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
import requests
from Propeht 

# 야후금융에서 주식정보를 제공하는 라이브러리 yfinance 이용
#  주식정보를 불러오고 차트 그리는거 합니다.

# 해당 주식의 트윗글들을 불러올수 있는 Api 가 있다.
# stockwit.com 에서 제공하는 Restful API 를 호출해서
# 데이터 가져오는것 실습

def main():
    st.header('Online Stock price Ticker')

    # yfinance 실행
    symbol=st.text_input('심볼 입력 : ')

    data=yf.Ticker(symbol)

    today=datetime.now().date().isoformat()
    print(today)

    df=data.history(start='2010-06-01',end=today)

    st.dataframe(df)

    st.subheader('종가')
    st.line_chart(df['Close'])

    st.subheader('거래양')
    st.line_chart(df['Volume'])

    # yfinance 라이브러리만의 정보
    # data.info
    # data.calendar
    # data.major_holders
    # data.institutional_holders
    # data.recommendations
    # data.dividends

    div_df=data.dividends
    st.dataframe(div_df.resample('Y').sum())

    new_df=div_df.reset_index()
    new_df['Year']=new_df['Date'].dt.year

    st.dataframe(new_df)

    fig=plt.figure()
    plt.bar(new_df['Year'],new_df['Dividends'])
    st.pyplot(fig)


    # 여러 주식 데이터를 한번에 보여주기.
    favorites=['msft','tsla','nvda','aapl','amzn']
    
    f_df=pd.DataFrame()

    for stock in favorites:
        f_df[stock]=yf.Ticker(stock).history(start='2010-01-01',end=today)['Close']
    
    st.dataframe(f_df)
    st.line_chart(f_df)

    # 스탁트윗의 API 를 호출
    res=requests.get('https://api.stocktwits.com/api/2/streams/symbol/{}.json'.format(symbol))
    
    # 제이슨 형식이므로 .json() 이용.
    res_data=res.json()

    # 파이썬의 딕셔너리와 리스트와의 조함
    # st.write(res_data)

    # for message in res_data['messages']:
    #     col1,col2=st.beta_columns([1,4])

    #     with col1:
    #         st.image(message['user']['avatar_url'])
    #     with col2:
    #         st.write('유저이름: '+message['user']['username'])
    #         st.write('트윗 내용: '+message['body'])
    #         st.write('올린시간: '+message['created_at'])

    p_df=df.reset_indec()
    p_df.rename(Columns={'Date':'ds','Close':'y'},inplace=True)
    # st.dataframe(p_df)
    
    m=Propeht()
    m.fit(p_df)
    
    future=m.make_future_dataframe(periods=365)
    forecast=m.predict(future)

    fig1=m.plot(fig1)
    st.pyplot(fig1)

    fig2=m.plot_components(forecast)
    st.pyplot(fig2)






if __name__=='__main__':
    main()