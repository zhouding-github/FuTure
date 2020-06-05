import requests
import 接口测试.BM预算系统.cfg as cfg
from pprint import pprint
import json


class ApiBM:

    def login(self, username, password):
        data = {
            'grant_type': 'password',
            'username': username,
            'password': password
        }
        req = requests.post(f'{cfg.ApiUrl}/api/Account/Login', data=data)
        return req.json()

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
        Properties = {
            'text01': self.Dictionary(Text01),
            'text02': self.Dictionary(Text02),
            'Code': Code
        }
        if Name is not None:
            Properties['name'] = Name
        if Name1 is not None:
            Properties['Name1'] = Name1
        if Count is not None:
            Properties['Count'] = Count
        if Notes is not None:
            Properties['Notes'] = Notes
        if SortId is not None:
            Properties['SortId'] = SortId

        return Properties

    # 获取辅助项信息
    def Dictionary(self, expressions_value):
        access_token = self.login('admin', '123@qwe')['access_token']
        hea = {
            'Authorization': f'bearer {access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {"expressions": [{"$type": "ModelPoint.Core.Filter.NamedFilter,ModelPoint2.Core",
                                 "filterName": "equals",
                                 "fieldTitle": "辅助项名称",
                                 "source": "filterPanel",
                                 "fieldName": "name",
                                 "value": expressions_value}],
                "sort": {"fieldName": "SortId",
                         },
                "pageSize": 20,
                "pageIndex": 0}
        req = requests.post(f'{cfg.ApiUrl}/api/entityQuery/'
                            f'Dictionary/query/Dictionary%7CDictionary',
                            data=json.dumps(data), headers=hea)
        Dictionarylist = req.json()['items'][0]
        del Dictionarylist['description']
        del Dictionarylist['enabled']
        del Dictionarylist['sortId']
        return Dictionarylist

    # 获取组织机构Code信息
    def Org_Cord(self, Org_name):
        access_token = self.login('admin', '123@qwe')['access_token']
        hea = {
            'Authorization': f'bearer {access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {
            "expressions": [{
                "$type": "ModelPoint.Core.Filter.NamedFilter,ModelPoint2.Core",
                "filterName": "equals",
                "fieldTitle": "名称",
                "source": "filterPanel",
                "fieldName": "name",
                "value": Org_name
            }],
            "sort": {
                "fieldName": "SortId",
                "desc": False,
                "requireOrder": True,
                "hasSortField": True
            },
            "pageSize": 20,
            "pageIndex": 0
        }
        req = requests.post(f'{cfg.ApiUrl}/api/entityQuery'
                            f'/Org/query/Org%7COrg',
                            headers=hea,
                            data=json.dumps(data))
        return req.json()['items'][0]['code']

    # 获取预算项的信息
    def BudgetAccountCode(self, BudgetAccountName,BudgetAccountGroup_Name):
        access_token = self.login('admin', '123@qwe')['access_token']
        hea = {
            'Authorization': f'bearer {access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {
            "expressions": [
                {
                    "$type": "ModelPoint.Core.Filter.NamedFilter,ModelPoint2.Core",
                    "filterName": "contains",
                    "fieldTitle": "预算项名称",
                    "source": "filterPanel",
                    "fieldName": "description",
                    "value": BudgetAccountName
                },{
                    "$type": "ModelPoint.Core.Filter.NamedFilter,ModelPoint2.Core",
                    "filterName": "equals",
                    "fieldTitle": "所属组",
                    "source": "filterPanel",
                    "fieldName": "budgetAccountGroup",
                    "value": self.BudgetAccountGroup(BudgetAccountGroup_Name)
                }
            ],
            "sort": {
                "fieldName": "SortId",
                "desc": False,
                "requireOrder": True,
                "hasSortField": True
            },
            "pageSize": 20,
            "pageIndex": 0
        }
        req = requests.post(f'{cfg.ApiUrl}/api/entityQuery/BudgetAccount/'
                            f'query/BudgetAccount%7CBankAccount',
                            headers=hea,
                            data=json.dumps(data))
        return req.json()['items'][0]['code']


    # Details的json转换
    def Details_List(self,
                     BudgetAccount_Name,
                     BudgetAccountGroup_Name,
                     Month1=None,
                     Month2=None,
                     Month3=None,
                     Month4=None,
                     Month5=None,
                     Month6=None,
                     Month7=None,
                     Month8=None,
                     Month9=None,
                     Month10=None,
                     Month11=None,
                     Month12=None):
        Details = {
            "BudgetAccountCode": self.BudgetAccountCode(BudgetAccount_Name,BudgetAccountGroup_Name)
        }
        if Month1 is not None:
            Details['Month1'] = Month1
        if Month2 is not None:
            Details['Month2'] = Month2
        if Month3 is not None:
            Details['Month3'] = Month3
        if Month4 is not None:
            Details['Month4'] = Month4
        if Month5 is not None:
            Details['Month5'] = Month5
        if Month6 is not None:
            Details['Month6'] = Month6
        if Month7 is not None:
            Details['Month7'] = Month7
        if Month8 is not None:
            Details['Month8'] = Month8
        if Month9 is not None:
            Details['Month9'] = Month9
        if Month10 is not None:
            Details['Month10'] = Month10
        if Month11 is not None:
            Details['Month11'] = Month11
        if Month12 is not None:
            Details['Month2'] = Month12
        return Details

        # 获取版本code
    def ScenarioCode(self, ScenarioCode):
        access_token = self.login('admin', '123@qwe')['access_token']
        hea = {
            'Authorization': f'bearer {access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {
            "expressions": [
                {
                    "$type": "ModelPoint.Core.Filter.NamedFilter,ModelPoint2.Core",
                    "filterName": "equals",
                    "fieldTitle": "名称",
                    "source": "filterPanel",
                    "fieldName": "name",
                    "value": ScenarioCode
                }
            ],
            "keyWord": None,
            "sort": {
                "fieldName": "SortId",
                "desc": False,
                "requireOrder": True,
                "hasSortField": True
            },
            "pageSize": 20,
            "pageIndex": 0
        }

        req = requests.post(f'{cfg.ApiUrl}/api/entityQuery/BudgetScenario/'
                            f'query/BudgetScenario%7CBudgetScenario',
                            headers=hea,
                            data=json.dumps(data))
        return req.json()['items'][0]['code']

    # 获得预算项组的信息，便于查询预算项的code
    def BudgetAccountGroup(self,BudgetAccountGroup_Name):
        access_token = self.login('admin', '123@qwe')['access_token']
        hea = {
            'Authorization': f'bearer {access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {"expressions": [{"$type": "ModelPoint.Core.Filter.NamedFilter,ModelPoint2.Core",
                                 "filterName": "equals",
                                 "fieldTitle": "预算项组名称",
                                 "source": "filterPanel",
                                 "fieldName": "name",
                                 "value": BudgetAccountGroup_Name}],
                "sort": {"fieldName": "SortId",
                         },
                "pageSize": 20,
                "pageIndex": 0}
        req = requests.post(f'{cfg.ApiUrl}/api/entityQuery/'
                            f'BudgetAccountGroup/query/_%7CBudgetAccountGroup',
                            data=json.dumps(data), headers=hea)
        acctGroupId = req.json()['items'][0]['acctGroupId']

        code = req.json()['items'][0]['code']
        Dictionarylist = {
              'acctGroupId': acctGroupId,
              'code': code,
              'name': BudgetAccountGroup_Name
        }
        return Dictionarylist

    def EmployeeAdministration(self,
                               Text01,  # 人员类别
                               Text02,  # 职工类别
                               Code,  # 代码
                               BudgetAccount_name,  # 预算项
                               BudgetAccountGroup_Name,  # 预算组
                               ScenarioCode,  # 版本编号
                               ENTITYNAME,  # 实体名称
                               Org_Name,  # 组织机构
                               Name=None,  # 名称
                               Name1=None,  # 别名
                               Count=None,  # 人数
                               Notes=None,  # 备注
                               SortId=None,  # 排序号
                               Month1=None,
                               Month2=None,
                               Month3=None,
                               Month4=None,
                               Month5=None,
                               Month6=None,
                               Month7=None,
                               Month8=None,
                               Month9=None,
                               Month10=None,
                               Month11=None,
                               Month12=None
                               ):
        access_token = self.login('admin', '123@qwe')['access_token']
        hea = {
            'Authorization': f'bearer {access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {
            "code": Code,
            "BudgetYear": 2019,
            "ScenarioCode": self.ScenarioCode(ScenarioCode),
            "OrgCode": self.Org_Cord(Org_Name),
            "Properties": self.Properties_json(Text01,
                                               Text02,
                                               Code,
                                               Name,
                                               Name1,
                                               Count,
                                               Notes,
                                               SortId),
            "Details": [self.Details_List(BudgetAccount_name,
                                          BudgetAccountGroup_Name,
                                          Month1,
                                          Month2,
                                          Month3,
                                          Month4,
                                          Month5,
                                          Month6,
                                          Month7,
                                          Month8,
                                          Month9,
                                          Month10,
                                          Month11,
                                          Month12)]
        }
        pprint(data)
        req = requests.post(f'{cfg.ApiUrl}/api-budget/BudgetSheet/{ENTITYNAME}',
                            headers=hea,
                            data=json.dumps(data))
        return req.json()


a = ApiBM()
po = a.EmployeeAdministration('在岗职工-企业领导人员',
                              '在职职工-委派人员',
                              'test002',
                              '培训费',
                              '管理条线',
                              '年度预算',
                              'EmployeeAdministration',
                              '党群工作部',
                              Name='测试计划',
                              Month1=89)
print("22222222222222")
pprint(po)

