# cart/views.py

from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        item = request.POST.get('item', '')  # itemがない場合はデフォルト値を空文字に設定
        if item == 'A':
            test = [1, 1980, 'スニーカー', 'converse', 'man']
        
        if item == 'B':
            test = [2, 980, 'サンダル', 'クロックス', 'unisex']
        
        self.add_to_cart(request, test)
        print(request.session['cart'])
        return render(request, "index.html")

    def add_to_cart(self, request, test):
        if 'cart' not in request.session:
            request.session['cart'] = []
        my_list = request.session.get('cart', [])
        # リストに要素を追加する
        my_list.append(test)
        # セッションにリストを保存する
        request.session['cart'] = my_list
def view_cart(request):
    cart_items = request.session.get('cart')
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

def kill_session(request):
    request.session.flush()
    print("sessionを消した")
    return render(request, "index.html")


