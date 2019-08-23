# Bixby: 버스 API 이용정보

## 사용서비스 목록

### 1. 버스 운행 정보 조회 서비스(busRouteInfo) API

- #### operations

  - ##### getStationByRoute: 노선별 경우 정류소 목록 조회

    - 요청: busRouteId

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRoute?busRouteId=30300001&serviceKey=서비스키
      ```

    - 응답: XML파일

      ```XML
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <BUSSTOP_ENG_NM>
      Chungnam National University, College of Agricultural College Terminal
      </BUSSTOP_ENG_NM>
      <BUSSTOP_NM>충대농대종점</BUSSTOP_NM>
      <BUSSTOP_SEQ>1</BUSSTOP_SEQ>
      <BUSSTOP_TP>1</BUSSTOP_TP>
      <BUS_NODE_ID>8002736</BUS_NODE_ID>
      <BUS_STOP_ID>42740</BUS_STOP_ID>
      <GPS_LATI>36.3661</GPS_LATI>
      <GPS_LONG>127.351875</GPS_LONG>
      <ROAD_NM></ROAD_NM>
      <ROAD_NM_ADDR></ROAD_NM_ADDR>
      <ROUTE_CD>30300001</ROUTE_CD>
      <TOTAL_DIST>148</TOTAL_DIST>
      </itemList>
      <itemList>
      <BUSSTOP_ENG_NM>Hanbit Apts.</BUSSTOP_ENG_NM>
      <BUSSTOP_NM>한빛아파트</BUSSTOP_NM>
      <BUSSTOP_SEQ>2</BUSSTOP_SEQ>
      <BUSSTOP_TP></BUSSTOP_TP>
      <BUS_NODE_ID>8002941</BUS_NODE_ID>
      <BUS_STOP_ID>42720</BUS_STOP_ID>
      <GPS_LATI>36.36286</GPS_LATI>
      <GPS_LONG>127.353004</GPS_LONG>
      <ROAD_NM></ROAD_NM>
      <ROAD_NM_ADDR></ROAD_NM_ADDR>
      <ROUTE_CD>30300001</ROUTE_CD>
      <TOTAL_DIST>501</TOTAL_DIST>
      </itemList>
      </msgBody>
      </ServiceResult>
      ```

      

  - ##### getStatioByRouteAll: 전체 노선별 경유 정류소 정보를 젱공하는 서비스

    - 요청: reqPage  요청페이지

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRouteAll?serviceKey= 서비스키&reqPage=1
      ```

    - 응답

      ```xml
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <BUSSTOP_ENG_NM>
      Chungnam National University, College of Agricultural College Terminal
      </BUSSTOP_ENG_NM>
      <BUSSTOP_NM>충대농대종점</BUSSTOP_NM>
      <BUSSTOP_SEQ>1</BUSSTOP_SEQ>
      <BUSSTOP_TP>1</BUSSTOP_TP>
      <BUS_NODE_ID>8002736</BUS_NODE_ID>
      <BUS_STOP_ID>42740</BUS_STOP_ID>
      <GPS_LATI>36.3661</GPS_LATI>
      <GPS_LONG>127.351875</GPS_LONG>
      <ROAD_NM></ROAD_NM>
      <ROAD_NM_ADDR></ROAD_NM_ADDR>
      <ROUTE_CD>30300001</ROUTE_CD>
      <TOTAL_DIST>148</TOTAL_DIST>
      </itemList>
      <itemList>
      <BUSSTOP_ENG_NM>Hanbit Apts.</BUSSTOP_ENG_NM>
      <BUSSTOP_NM>한빛아파트</BUSSTOP_NM>
      <BUSSTOP_SEQ>2</BUSSTOP_SEQ>
      <BUSSTOP_TP></BUSSTOP_TP>
      <BUS_NODE_ID>8002941</BUS_NODE_ID>
      <BUS_STOP_ID>42720</BUS_STOP_ID>
      <GPS_LATI>36.36286</GPS_LATI>
      <GPS_LONG>127.353004</GPS_LONG>
      <ROAD_NM></ROAD_NM>
      <ROAD_NM_ADDR></ROAD_NM_ADDR>
      <ROUTE_CD>30300001</ROUTE_CD>
      <TOTAL_DIST>501</TOTAL_DIST>
      </itemList>
      </msgBody>
      </ServiceResult>
      
      ```

      

  - ##### getRouteInfo: 노선정보 상세 조회 오퍼레이션 명세

    - 요청: busRouteId(버스노선 ID)

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getRouteInfo?busRouteId=30300001&serviceKey=서비스키
      ```

    - 응답

      ```xml
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <ALLO_INTERVAL>25</ALLO_INTERVAL>
      <ALLO_INTERVAL_SAT>25</ALLO_INTERVAL_SAT>
      <ALLO_INTERVAL_SUN>30</ALLO_INTERVAL_SUN>
      <BUSSTOP_CNT>104</BUSSTOP_CNT>
      <END_NODE_ID>8002737</END_NODE_ID>
      <END_STOP_ID>42750</END_STOP_ID>
      <ORIGIN_END>2230</ORIGIN_END>
      <ORIGIN_END_SAT>2230</ORIGIN_END_SAT>
      <ORIGIN_END_SUN>2230</ORIGIN_END_SUN>
      <ORIGIN_START>0600</ORIGIN_START>
      <ORIGIN_START_SAT>0600</ORIGIN_START_SAT>
      <ORIGIN_START_SUN>0630</ORIGIN_START_SUN>
      <ROUTE_CD>30300001</ROUTE_CD>
      <ROUTE_NO>1</ROUTE_NO>
      <ROUTE_TP>5</ROUTE_TP>
      <RUN_DIST_HALF>23.9555</RUN_DIST_HALF>
      <RUN_TM>65</RUN_TM>
      <START_NODE_ID>8002736</START_NODE_ID>
      <START_STOP_ID>42740</START_STOP_ID>
      <TURN_END>2230</TURN_END>
      <TURN_END_SAT>2230</TURN_END_SAT>
      <TURN_END_SUN>2230</TURN_END_SUN>
      <TURN_NODE_ID>8007228</TURN_NODE_ID>
      <TURN_START>0600</TURN_START>
      <TURN_START_SAT>0600</TURN_START_SAT>
      <TURN_START_SUN>0630</TURN_START_SUN>
      <TURN_STOP_ID>82370</TURN_STOP_ID>
      </itemList>
      </msgBody>
      </ServiceResult>
      ```

  - ##### getRouteInfoAll: 전체 노선별 노선정보 조회 오퍼레이션 명세

    - 요청: reqPage(요청페이지 번호)

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getRouteInfoAll? serviceKey=서비스키&reqPage=1
      ```

    - 응답

      ```xml
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <ALLO_INTERVAL>25</ALLO_INTERVAL>
      <ALLO_INTERVAL_SAT>25</ALLO_INTERVAL_SAT>
      <ALLO_INTERVAL_SUN>30</ALLO_INTERVAL_SUN>
      <BUSSTOP_CNT>104</BUSSTOP_CNT>
      <END_NODE_ID>8002737</END_NODE_ID>
      <END_STOP_ID>42750</END_STOP_ID>
      <ORIGIN_END>2230</ORIGIN_END>
      <ORIGIN_END_SAT>2230</ORIGIN_END_SAT>
      <ORIGIN_END_SUN>2230</ORIGIN_END_SUN>
      <ORIGIN_START>0600</ORIGIN_START>
      <ORIGIN_START_SAT>0600</ORIGIN_START_SAT>
      <ORIGIN_START_SUN>0630</ORIGIN_START_SUN>
      <ROUTE_CD>30300001</ROUTE_CD>
      <ROUTE_NO>1</ROUTE_NO>
      <ROUTE_TP>5</ROUTE_TP>
      <RUN_DIST_HALF>23.9555</RUN_DIST_HALF>
      <RUN_TM>65</RUN_TM>
      <START_NODE_ID>8002736</START_NODE_ID>
      <START_STOP_ID>42740</START_STOP_ID>
      <TURN_END>2230</TURN_END>
      <TURN_END_SAT>2230</TURN_END_SAT>
      <TURN_END_SUN>2230</TURN_END_SUN>
      <TURN_NODE_ID>8007228</TURN_NODE_ID>
      <TURN_START>0600</TURN_START>
      <TURN_START_SAT>0600</TURN_START_SAT>
      <TURN_START_SUN>0630</TURN_START_SUN>
      <TURN_STOP_ID>82370</TURN_STOP_ID>
      </itemList>
      </msgBody>
      </ServiceResult>
      ```

    

---



### 2. 버스 정류장 정보 조회 서비스 API (stationinfo)

- #### operatioin

  - ##### getStationByStopID: 정류소ID(7자리)별 정류소 정보 조회 

    - 요청:BusStopID

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/stationinfo/getStationByStopID?BusStopID=8001378&serviceKey=서비스키
      ```

    - 응답

      ```xml
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <ARO_BUSSTOP_ID>32350</ARO_BUSSTOP_ID>
      <BUSSTOP_ENG_NM>Daejeon City Hall</BUSSTOP_ENG_NM>
      <BUSSTOP_NM>대전광역시청</BUSSTOP_NM>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <GPS_LATI>36.351112</GPS_LATI>
      <GPS_LONG>127.384865</GPS_LONG>
      <ROAD_NM>둔산로</ROAD_NM>
      <ROAD_NM_ADDR></ROAD_NM_ADDR>
      <ROUTE_NO>104, 106, 316, 617, 703, 705, 911, 918</ROUTE_NO>
      </itemList>
      </msgBody>
      </ServiceResult>
      ```

      

  - getStationByUid: 정류소ID(5자리)별 정류소 정보 조회

    - 요청: arsId

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/stationinfo/getStationByUid?arsId=32350&serviceKey=서비스키
      ```

    - 응답

      ```xml
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <ARO_BUSSTOP_ID>32350</ARO_BUSSTOP_ID>
      <BUSSTOP_ENG_NM>Daejeon City Hall</BUSSTOP_ENG_NM>
      <BUSSTOP_NM>대전광역시청</BUSSTOP_NM>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <GPS_LATI>36.351112</GPS_LATI>
      <GPS_LONG>127.384865</GPS_LONG>
      <ROAD_NM>둔산로</ROAD_NM>
      <ROAD_NM_ADDR></ROAD_NM_ADDR>
      <ROUTE_NO>104, 106, 316, 617, 703, 705, 911, 918</ROUTE_NO>
      </itemList>
      </msgBody>
      </ServiceResult>
      
      ```

      

---



### 3. 버스 위치정보 조회 서비스(busposinfo)

- #### operation

  - ##### getBusPosByRtid: 노선별 버스 위치정보 조회 오퍼레이션 명세

    - 요청: busRouteId(노선ID)

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/busposinfo/getBusPosByRtid?busRouteId=30300001&serviceKey=서비스키
      ```

    - 응답

      ```xml
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <ARR_TIME>20151116143853</ARR_TIME>
      <BUS_NODE_ID>8001590</BUS_NODE_ID>
      <BUS_STOP_ID>41210</BUS_STOP_ID>
      <DIR>1</DIR>
      <EVT_CD>1</EVT_CD>
      <GPS_LATI>36.354805</GPS_LATI>
      <GPS_LONG>127.337681</GPS_LONG>
      <ROUTE_CD>30300001</ROUTE_CD>
      <STRE_DT>20151116143855</STRE_DT>
      <TOTAL_DIST>44995</TOTAL_DIST>
      <ud_type>1</ud_type>
      </itemList>
      <itemList>
      <ARR_TIME>20151116143920</ARR_TIME>
      <BUS_NODE_ID>8002410</BUS_NODE_ID>
      <BUS_STOP_ID>41290</BUS_STOP_ID>
      <DIR>0</DIR>
      <EVT_CD>1</EVT_CD>
      <GPS_LATI>36.3542</GPS_LATI>
      <GPS_LONG>127.340253</GPS_LONG>
      <ROUTE_CD>30300001</ROUTE_CD>
      <STRE_DT>20151116143924</STRE_DT>
      <TOTAL_DIST>2908</TOTAL_DIST>
      <ud_type>0</ud_type>
      </itemList>
      <itemList>
      <ARR_TIME>20151116143858</ARR_TIME>
      <BUS_NODE_ID>8002767</BUS_NODE_ID>
      <BUS_STOP_ID>44290</BUS_STOP_ID>
      <DIR>1</DIR>
      <EVT_CD>1</EVT_CD>
      <GPS_LATI>36.409226</GPS_LATI>
      <GPS_LONG>127.395466</GPS_LONG>
      <ROUTE_CD>30300001</ROUTE_CD>
      <STRE_DT>20151116143902</STRE_DT>
      <TOTAL_DIST>29336</TOTAL_DIST>
      <ud_type>1</ud_type>
      </itemList>
      </msgBody>
      </ServiceResult>
      ```

      

---

### 4. 정류장 버스 도착 정보 조회 서비스 API(arrive)

- #### operation

  - getArrInfoByStopID: 정류소ID(7자리) 별 버스 도착예정정보 조회 서비스

    - 요청:  BusStopID(정류소 ID 7자리)

      ```
      http://openapitraffic.daejeon.go.kr/api/rest/arrive/getArrInfoByStopID?busStopID=8001378&serviceKey=서비스키
      ```

      

  - getArrInfoByUid: 정류소ID(5자리) 별 버스 도착예정정보 조회 서비스

    - 요청:  arsId(정류소 ID 5자리)

      ```
       http://openapitraffic.daejeon.go.kr/api/rest/arrive/getArrInfoByUid?arsId=32350&serviceKey=서비스키
      ```

      

    - 응답

      ```xml
      <ServiceResult>
      <comMsgHeader/>
      <msgHeader>
      <headerCd>0</headerCd>
      <headerMsg>정상적으로 처리되었습니다.</headerMsg>
      <currentPage>1</currentPage>
      <itemCnt>1</itemCnt>
      <itemPageCnt>1</itemPageCnt>
      </msgHeader>
      <msgBody>
      <itemList>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <BUS_STOP_ID>32350</BUS_STOP_ID>
      <CAR_REG_NO>대전75자3378</CAR_REG_NO>
      <DESTINATION>비래동</DESTINATION>
      <EXTIME_MIN>6</EXTIME_MIN>
      <EXTIME_SEC>317</EXTIME_SEC>
      <INFO_OFFER_TM>2015-11-16 15:01:09.0</INFO_OFFER_TM>
      <LAST_CAT>3</LAST_CAT>
      <LAST_STOP_ID>32050</LAST_STOP_ID>
      <MSG_TP>03</MSG_TP>
      <ROUTE_CD>30300041</ROUTE_CD>
      <ROUTE_NO>106</ROUTE_NO>
      <ROUTE_TP>2</ROUTE_TP>
      <STATUS_POS>2</STATUS_POS>
      <STOP_NAME>대전광역시청</STOP_NAME>
      </itemList>
      <itemList>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <BUS_STOP_ID>32350</BUS_STOP_ID>
      <CAR_REG_NO>대전75자9814</CAR_REG_NO>
      <DESTINATION>신탄진</DESTINATION>
      <EXTIME_MIN>4</EXTIME_MIN>
      <EXTIME_SEC>190</EXTIME_SEC>
      <INFO_OFFER_TM>2015-11-16 15:03:26.0</INFO_OFFER_TM>
      <LAST_CAT>3</LAST_CAT>
      <LAST_STOP_ID>32100</LAST_STOP_ID>
      <MSG_TP>03</MSG_TP>
      <ROUTE_CD>30300087</ROUTE_CD>
      <ROUTE_NO>703</ROUTE_NO>
      <ROUTE_TP>2</ROUTE_TP>
      <STATUS_POS>3</STATUS_POS>
      <STOP_NAME>대전광역시청</STOP_NAME>
      </itemList>
      <itemList>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <BUS_STOP_ID>32350</BUS_STOP_ID>
      <CAR_REG_NO>대전75자3526</CAR_REG_NO>
      <DESTINATION>대한통운</DESTINATION>
      <EXTIME_MIN>4</EXTIME_MIN>
      <EXTIME_SEC>204</EXTIME_SEC>
      <INFO_OFFER_TM>2015-11-16 15:03:37.0</INFO_OFFER_TM>
      <LAST_CAT>3</LAST_CAT>
      <LAST_STOP_ID>32100</LAST_STOP_ID>
      <MSG_TP>03</MSG_TP>
      <ROUTE_CD>30300060</ROUTE_CD>
      <ROUTE_NO>316</ROUTE_NO>
      <ROUTE_TP>2</ROUTE_TP>
      <STATUS_POS>3</STATUS_POS>
      <STOP_NAME>대전광역시청</STOP_NAME>
      </itemList>
      <itemList>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <BUS_STOP_ID>32350</BUS_STOP_ID>
      <CAR_REG_NO>대전75자9518</CAR_REG_NO>
      <DESTINATION>비래동</DESTINATION>
      <EXTIME_MIN>16</EXTIME_MIN>
      <EXTIME_SEC>902</EXTIME_SEC>
      <INFO_OFFER_TM>2015-11-16 15:03:48.0</INFO_OFFER_TM>
      <LAST_CAT>3</LAST_CAT>
      <LAST_STOP_ID>31630</LAST_STOP_ID>
      <MSG_TP>03</MSG_TP>
      <ROUTE_CD>30300081</ROUTE_CD>
      <ROUTE_NO>617</ROUTE_NO>
      <ROUTE_TP>2</ROUTE_TP>
      <STATUS_POS>9</STATUS_POS>
      <STOP_NAME>대전광역시청</STOP_NAME>
      </itemList>
      <itemList>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <BUS_STOP_ID>32350</BUS_STOP_ID>
      <CAR_REG_NO>대전75자9682</CAR_REG_NO>
      <DESTINATION>탄방역</DESTINATION>
      <EXTIME_MIN>11</EXTIME_MIN>
      <EXTIME_SEC>616</EXTIME_SEC>
      <INFO_OFFER_TM>2015-11-16 15:03:56.0</INFO_OFFER_TM>
      <LAST_CAT>3</LAST_CAT>
      <LAST_STOP_ID>32890</LAST_STOP_ID>
      <MSG_TP>03</MSG_TP>
      <ROUTE_CD>30300039</ROUTE_CD>
      <ROUTE_NO>104</ROUTE_NO>
      <ROUTE_TP>2</ROUTE_TP>
      <STATUS_POS>6</STATUS_POS>
      <STOP_NAME>대전광역시청</STOP_NAME>
      </itemList>
      <itemList>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <BUS_STOP_ID>32350</BUS_STOP_ID>
      <CAR_REG_NO>대전75자2056</CAR_REG_NO>
      <DESTINATION>대전역</DESTINATION>
      <EXTIME_MIN>9</EXTIME_MIN>
      <EXTIME_SEC>486</EXTIME_SEC>
      <INFO_OFFER_TM>2015-11-16 15:03:50.0</INFO_OFFER_TM>
      <LAST_CAT>3</LAST_CAT>
      <LAST_STOP_ID>32980</LAST_STOP_ID>
      <MSG_TP>03</MSG_TP>
      <ROUTE_CD>30300089</ROUTE_CD>
      <ROUTE_NO>705</ROUTE_NO>
      <ROUTE_TP>2</ROUTE_TP>
      <STATUS_POS>5</STATUS_POS>
      <STOP_NAME>대전광역시청</STOP_NAME>
      </itemList>
      <itemList>
      <BUS_NODE_ID>8001378</BUS_NODE_ID>
      <BUS_STOP_ID>32350</BUS_STOP_ID>
      <CAR_REG_NO>대전75자2349</CAR_REG_NO>
      <DESTINATION>스마트시티</DESTINATION>
      <EXTIME_MIN>18</EXTIME_MIN>
      <EXTIME_SEC>1061</EXTIME_SEC>
      <INFO_OFFER_TM>2015-11-16 15:01:30.0</INFO_OFFER_TM>
      <LAST_CAT>3</LAST_CAT>
      <LAST_STOP_ID>41270</LAST_STOP_ID>
      <MSG_TP>03</MSG_TP>
      <ROUTE_CD>30300094</ROUTE_CD>
      <ROUTE_NO>911</ROUTE_NO>
      <ROUTE_TP>3</ROUTE_TP>
      <STATUS_POS>11</STATUS_POS>
      <STOP_NAME>대전광역시청</STOP_NAME>
      </itemList>
      </msgBody>
      </ServiceResult>
      ```

