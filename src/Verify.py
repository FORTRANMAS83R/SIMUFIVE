def VerifyRate(hp_Rate,hc_Rate):
    if(hp_Rate>1 or hc_Rate>1):
        raise ValueError("Rate should be less than 1")
    if(hp_Rate<0 or hc_Rate<0):
        raise ValueError("Rate should be greater than 0")
    return True

def VerifySubVal(sub_rate):
    if(sub_rate>1):
        raise ValueError("Subscription rate should be less than 1")
    if(sub_rate<0):
        raise ValueError("Subscription rate should be greater than 0")
    return True