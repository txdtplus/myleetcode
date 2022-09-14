nums_str = input()
nums_list = nums_str.split('.')

nums_int = nums_list[0]
nums_frac = nums_list[1]
out = "人民币"
dict1 = {'1':'壹',
        '2':'贰',
        '3':'叁',
        '4':'肆',
        '5':'伍',
        '6':'陆',
        '7':'柒',
        '8':'捌',
        '9':'玖',
        '0':'零'
        }

dict2 = {
         9:'亿',
         5:'万',
         4:'仟',
         3:'佰',
         2:'拾',
         1:''
        }

def less_wan_num(nums_str):
    out = ""
    scale = len(nums_str)
    for i in range(len(nums_str)):
        num_tmp = dict1[nums_str[i]]
        if scale > 1:
            scale_tmp = dict2[scale]
        else:
            scale_tmp = ''
        
        if nums_str[i] != '0':
            if nums_str[i] == '1' and scale_tmp == '拾':
                out = out + scale_tmp
            else:
                out = out + num_tmp + scale_tmp
        else:
            if out[-1] != '零':
                if scale != 1:
                    out = out + num_tmp
        
        scale -= 1
    return out

if len(nums_int) != 1:
    if len(nums_int)  <= 4:
        out = out + less_wan_num(nums_int)
    elif 4 < len(nums_int)  <= 8:
        num_small = nums_int[-4:]
        num_large = nums_int[:-4]
        out = out + less_wan_num(num_large) + '万' + less_wan_num(num_small)
    out = out + '元'
else:
    if nums_int != '0':
        out = out + dict1[nums_int] + '元'
    

if int(nums_frac) == 0:
    out = out + '整'
else:
    if nums_frac[0] != '0':
        out = out + dict1[nums_frac[0]] + '角'
    if nums_frac[1] != '0':
        out = out + dict1[nums_frac[1]] + '分'

print(out)