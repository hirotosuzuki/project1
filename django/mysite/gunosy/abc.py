import naivebayes
siteurl="https://gunosy.com/articles/albEa"
text=naivebayes.url_to_sepatext(siteurl)
print(text)
print(naivebayes.classify(text))



try:
    siteurl = request.GET.get('site_url')
    text = gunosy.naivebayes.url_to_sepatext(siteurl)
    category = gunosy.naivebayes.classify(text)
    d = {
        'category':category,
    }
    return render(request,'get_url.html',d)
except:
    false='正しくURLを入力してください'
    d = {
        'false':false,
    }
    return render(request,'get_url.html',d)
