

function changeColor()
{
    document.getElementById("text1").style.color='blue'
    document.getElementById("text2").style.color='yellow'
    document.getElementById("text3").style.color='red'
}
function changeBgColor(color)

{
    
    return document.body.style.background= color
}

function copyContent(paragraph1, paragraph2)
{
    var paragraph1 = document.querySelectorAll('p')[0]
    var paragraph2 =  document.querySelectorAll('p')[1]
    return paragraph1.innerHTML=paragraph2.innerHTML
}
function changeFontSize(x)
{
    return document.getElementsByTagName('p')[0].style.fontSize =x+'px'
    return document.getElementsByTagName('p')[1].style.fontSize =x+'px'
    return document.getElementsByTagName('p')[2].style.fontSize =x+'px'
}
function increaseFontSize(paragraph)
{
    var el=document.getElementsByTagName('p')[paragraph]
    var size=window.getComputedStyle(el, null).getPropertyValue('font-size')
    var size = parseFloat(size)
    size+=1
    if (size>30)
    {
        return ("Lỗi vượt quá 30px")
    }
    else{
       el.style.fontSize=size+'px'

    }

   
}

function decreaseFontSize(paragraph)
{
    var el=document.getElementsByTagName('p')[paragraph]
    var size=window.getComputedStyle(el, null).getPropertyValue('font-size')
    var size = parseFloat(size)
    size-=1
    if (size<10)
    {
        return ("Lỗi vượt quá 30px")
    }
    else{
       el.style.fontSize=size+'px'

    }

   
}