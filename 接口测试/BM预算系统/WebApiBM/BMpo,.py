from 接口测试.BM预算系统.WebApiBM.ApiBM import ApiBM


class BMpo(ApiBM):
    def login(self,username,password):
        ApiBM.login(username,password)