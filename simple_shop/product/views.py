from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from .models import Product
from .forms import ProductRegisterForm
from order.forms import OrderForm

# 장고의 대표적인 제네릭 뷰인 ListView
#   단순히 리스팅할 모델의 클래스를 지정해주는 것만으로
#   해당 모델에 들어있는 데이터를 템플릿에 리스팅할 수 있게 도와준다.
class ProductList(ListView):
    # queryset = Product.objects.all()과 똑같음
    model = Product
    template_name = 'product_list.html'
    
    # product_list.html에서 object_list로 for문을 돌린다.
    #   => ListView에서 모델에 있는 모든 데이터 조회 결과는 object_list 내의 QuerySet 형식으로 템플릿에 넘어가게 되기 때문에 object_list를 for문으로 하나씩 객체 추출하여 표현
    #   이때 object_list 변수를 템플릿에서 사용하지 않으려면 아래와 같이 context_object_name 활용

    context_object_name = 'product_list'

class ProductRegister(FormView):
    form_class = ProductRegisterForm
    template_name = 'product_reg.html'
    success_url='/product/'

class ProductDetail(DetailView):
    template_name = 'product_detail.html'

    # queryset 필드는 모델 조회에 의해 표시되는 뷰에는 어디든 사용 가능 (ex. DetailView, ListView 등)
    # DetailView의 queryset == 조회 대상이 될 데이터들의 집합
    #   현재 프로젝트에선 모든 데이터가 조회 대상이 되기 때문에 all() 사용
    #   pk가 들어왔을때, 해당 pk인 상품 한 개만 조회된다. 
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context['form'] = OrderForm(self.request)
        return context