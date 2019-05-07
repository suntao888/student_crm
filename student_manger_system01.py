class StudentModel:
    def __init__(self,id=0,name="", age=0,score=0):
        self.id = id
        self.name = name
        self.age=age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    # def print_self(self):
    #     print(self.id, self.name, self.age,self.score)

class StudentManagerController:
    def __init__(self):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu


    def add_student(self,stu):
        stu.id=len(self.list_stu)+1
        self.list_stu.append(stu)

    def remove_student(self, id):
        for item in self.__list_stu:
            if item.id==id:
               self.__list_stu.remove(item)

    def update_student(self,stu_info):
        for i in self.__list_stu:
            if i.id==stu_info.id:
               i.name=stu_info.name
               i.age=stu_info.age
               i.score=stu_info.score
               return  True
        return False


    def order_score(self):
        # new_list = self.__list_stu[:]
        # for r in range(len(new_list) - 1):
        #     for c in range(r + 1, len(new_list)):
        #         if new_list[r].score < new_list[c].score:
        #             new_list[r], new_list[c] = new_list[c], new_list[r]
        # return new_list

        for i in range(len(self.__list_stu)-1):
            for j in range(i+1,len(self.__list_stu)):
                if self.__list_stu[i].score<self.__list_stu[j].score:
                    self.__list_stu[i],self.__list_stu[j]=self.__list_stu[j],self.__list_stu[i]
                return True
        return  False


#
# # 添加
# ui=StudentMangerController()
# st=StudentModel(name="suntao",age=24,score=10)
# ui.add_student(st)
# st1=StudentModel(name="zs")
# ui.add_student(st1)
#
# #删除
# # st2=StudentModel(id=2)
# # ui.remove_student(st2)
#
# #update
# st2=StudentModel(2,"ww",100,100)
# ui.update_student(st2)
# ui.order_score()
# #order
# # order_score()
#
# for item in ui.list_stu:
#     print(item.id,item.name,item.age,item.score)


class StudentManagerView:
    """
        学生管理器视图类
    """
    def __init__(self):
        # 创建学生管理控制器对象
        self.__controller = StudentManagerController()


    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("---------------------")
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩降序显示")
        print("---------------------")

    def __select_menu(self):
        """
            选择菜单
        :return:
        """
        number = input("请输入选项：")
        if number == "1":
            self.input_add()

        elif number =="2":
            self.cat(self.__controller.list_stu)
            # for item in self.__controller.list_stu:
            #     print(item.id, item.name, item.age, item.score)
        elif number == "3":
            self.del_stu()
        elif number == "4":
            self.up_stu()
        elif number == "5":
            self.order(self.__controller.list_stu)

    def main(self):
        """
            学生管理器入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def cat(self, list_stu):

        for item in list_stu:
            print("%d | %s | %d | %d" % (item.id, item.name, item.age, item.score))

    def input_add(self):

        while True:
            stu=StudentModel()
            stu.name = input("请输入学生姓名")
            stu.age = int(input("请输入学生年龄"))
            stu.score = int(input("请输入学生成绩"))
            self.__controller.add_student(stu)
            stop = input("输入y继续")
            if stop != "y":
                break

    def del_stu(self):

        id = int(input("请输入删除学生的ｉd"))
        result = self.__controller.remove_student(id )
        if True:
            print("ok")
        else:
            print("no")


    def up_stu(self):

        stu_info = StudentModel()
        stu_info.id = int(input("请输入修改学生的ｉd"))
        stu_info.name = input("请输入学生姓名")
        stu_info.age = int(input("请输入学生年龄"))
        stu_info.score = int(input("请输入学生成绩"))
        self.__controller.update_student(stu_info)


    def order(self,list_stu):

            self.__controller.order_score()



view = StudentManagerView()
view.main()













