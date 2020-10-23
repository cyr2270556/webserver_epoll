#session检查
def session_check(request,target):
    """
    target:检查对象(session的键)(str类型)
    检查session是否存在
    :return:true
    """
    if target in request.session:
        return True
    else:
        return False

#cookie检查
def cookie_check(request,target):
    """
    :param request:
    :param target: 检查对象(cookies名字)(str类型)
    :return:
    """
    temp=request.COOKIES.get(target)
    if temp:
        return True
    else:
        return False


