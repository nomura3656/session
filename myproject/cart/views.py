# cart/views.py

from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        item = request.POST.get('item', '')  # itemがない場合はデフォルト値を空文字に設定
        self.add_to_cart(request, item)
        print(request.session['cart'])
        return render(request, "index.html")

    def add_to_cart(self, request, item):
        if 'cart' not in request.session:
            request.session['cart'] = []
        my_list = request.session.get('cart', [])
        # リストに要素を追加する
        my_list.append(item)
        # セッションにリストを保存する
        request.session['cart'] = my_list
def view_cart(request):
    cart_items = request.session.get('cart')
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})
