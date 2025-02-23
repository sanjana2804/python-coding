def anagram(str1,str2):
    if len(str1) != len(str2):
        print("They are not anagram")
    else:
        count1={ }
        count2={ }
        for i in str1:
          if i in count1:
            count1[i]+=1
          else:
            count1[i]=1
        for j in str2:
          if j in count2:
            count2[j]+=1
          else:
              count2[j]=1
        if count1==count2:
            print("they are anagram")
        else:
            print("not anagram")

str1=input("enter string 1:")
str2=input("enter string 2:")
anagram(str1,str2)

      
