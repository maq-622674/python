#改版前
def function(arg1="",arg2=""):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print(type(arg1))

function("Hello","World")

function()

#改版后
def foo(*args):
    print(args)
    print(type(args))
    #numargs=len(args)
    #print("NUmber of arguments:",numargs)
   # for i,x in enumerate(args):
        #print("Argument%sis:%s"%(i,x))

foo()
foo("hello")
foo("hello","World","Again",'')