import pywhatkit as pw

txt = input("Enter Your Text : ")

if (len(txt) == 0):
    txt = """ she is mess , she's messiah
            the more she is kind,
            and a bit cute,
            with a beautiful mind.

            moreover she is sassy 
            and thats what makes me fall,
            I've fallen for her her madness 
            and the beauty of mind at all.

            Her mind is full of love 
            and her eyes are those damn stars,
            when she gets me alone ,
            she leaves me with them scars.

            Oh, my love you are Ocean of Kindness 
            and Im thirsty enough to drink it all
            would you let me taste your water ,
            Ah ! It's Elixir what they call."""
else:
    txt = txt

pw.text_to_handwriting(txt, "Handwriting.png", [0, 0, 138])
print("*** End ***")
