
# s = "hello world" 
# # O/P: "OLLEH DLROW"

# string = s.split()
# print(string)
# op=[]
# for ele in string:
#     op.append(ele[::-1].upper())
    
# print(" ".join(op))

# for ele in string:
# 	i = ele[::-1].upper()
	
# for ch in s:
# 	print(s[::-1].upper())
	

list_ = [1,2,3,4,3,6,7,5,6]
# print(set(list))
_l=[]
# for ele in list:
#     if ele not in _l:
#         _l.append(ele)
# print(_l)

# for ele in list:
#     if list.count(str(ele))==1:
#         _l.append(ele)
# print(_l)

l = [ele for ele in list if list_.count(str(ele))==1] 
print(l) 

