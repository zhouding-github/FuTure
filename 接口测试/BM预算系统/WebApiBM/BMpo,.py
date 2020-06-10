from 接口测试.BM预算系统.WebApiBM.ApiBM import ApiBM


class BMpo(ApiBM):
    def login(self,username,password):
        ApiBM.login(username,password)
    def Properties_json(self,
                        Text01,  # 人员类别
                        Text02,  # 职工类别
                        Code,  # 代码
                        Name=None,  # 名称
                        Name1=None,  # 别名
                        Count=None,  # 人数
                        Notes=None,  # 备注
                        SortId=None  # 排序号
                        # Line=None,  #所属条线
                        # IsPlanning=None,  #是否计划
                        # Status=None,  #状态
                        # BudgetStatus=None,  #预算状态
                        # Position=None,  #职位
                        # Post=None,  #岗位
                        ):
         ApiBM.Properties_json()