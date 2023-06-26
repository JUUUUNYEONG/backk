x=[42,40,38,37,43,39,78,38,45,44,40,38,41,35,31,44]

def cv(x):
    n=len(x)
    m=sum(x)
    M=m/len(x)
    V=sum([(x_i - M)**2 for x_i in x])/(n-1)
    s=V**(1/2)
    return((s/M)*100)
print(cv(x))
N=len(x)
for i in range(N):
    for j in range(i,N,1): #제일 작은 수를 첫번째로 보내는 과정
        if x[i] > x[j]:
            tmp=x[i] #보낼 값 저장 # 최솟값이 아니다, 지역 최솟값
            x[i]=x[j] #지역 최솟값 x[i]가 더 작은 수로 바뀌었다.
            x[j]=tmp
print(x)

