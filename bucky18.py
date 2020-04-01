def health_calc(age, apples, cig):
    ans=(100-age)+(apples*20)+(cig*2)
    print(ans)

puneet=(28,200,0)
health_calc(puneet[0], puneet[1], puneet[2])
health_calc(*puneet)