# Clustering

데이터를 유사도에 따라 k개의 그룹으로 나눈 것

추천시스템에 주로 활용된다.



### K-means Clustering

* k개의 평균점

* Cluster 사이즈가 작거나 크면 정확도 ↓

* 평균점으로부터 공모양의 데이터만 잘 찾을 수 있다.



### Hierarchical Clustering

* 많은 Cluster를 만든 후 가까운 두 개의 Cluster를 merge하면서 Cluster의 개수를 k개까지 줄인다.

* Cluster간의 거리 계산법에 따라 결과가 달라진다.
  * single-link : 가장 짧은 거리
  * mean-link: cluster의  average-link, centroid-link



### Density Based Clustering

(DBSCAN Clustering)

epsilon과 minpoints에 따라 다른 밀도와 다른 개수의 그룹이 생긴다.



## EM Clustering Algorithm

E-step for EM algorithm