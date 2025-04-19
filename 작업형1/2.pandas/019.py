# 19. 데이터프레임 합치기

# 1. 단순병합: concat()
    # - axis=0(기본값): 위-아래로 합침, axis=1: 왼-오 합침
    # - ignore_index = True : 인덱스를 새롭게 설정
    # pd.concat([컬럼명1, 컬럼명2], axis=1, ignore_index=True)

# 2. 키(Key)기준 병합: merge()
    # - pd.merge(컬럼명1, 컬럼명2, on="기준이될 키값")