from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('ajax/load-cities', views.load_city, name="load_city"),
    path('ajax/load-state', views.load_state, name="load_state"),
    path('ajax/fetch_pdt', views.fetch_pdt, name="fetch_pdt"),
    path('ajax/load-creator/<ins_by>', views.load_creator, name="load_creator"),
    path('contact/', views.contact, name="contact"),
    path('designs/', views.designs, name="designs"),
    path('user_dashboard/', views.user_dashboard, name="user_dashboard"),
    path('admin/design_element/', views.design_element, name="design_element"),
    path('product_list/', views.product_list, name="product_list"),
    path('product/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('product/<pdt_id>', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('ajax/addtocart', views.addtocart, name="addtocart"),
    path('ajax/addtocart/update', views.update_addtocart, name="update_addtocart"),
    path('product_list/', views.product_list, name="product_list"),
    path('admin/design_element/', views.design_element, name="design_element"),
    path('checkout/', views.checkout, name="checkout"),
    path('order/', views.order, name="order"),
    path('addAddress/', views.addAddress, name="addAddress"),
    path('placeOrder/', views.placeOrder, name="placeOrder"),
    path('designProduct/<design_id>', views.designProduct, name="designProduct"),
    # path('order_test/', views.order_test, name="order"),
    path('designer/login/', views.designer_login, name="designer_login"),
    path('chat/', views.chat, name="chat"),
    path('designer/chat/', views.designer_chat, name="designer_chat"),
    path('ajax/chat/getMsgs/<user_id>', views.getMsgs, name="getMsgs"),
    path('ajax/chat/getChatList/', views.getChatList, name="getChatList"),
    path('ajax/chat/send_msg/', views.send_msg, name="send_msg"),
    path('ajax/chat/getUnseenMsg/', views.getUnseenMsg, name="getUnseenMsg"),
    path('ajax/chat/unseenCnt/', views.unseenCnt, name="unseenCnt"),
    path('ajax/chat/sendAttach/', views.sendAttach, name="sendAttach"),
    path('designer_dashboard/', views.designer_dashboard, name="designer_dashboard"),
    path('designer_design/', views.designer_design, name="designer_design"),
    path('designer_design/add', views.designer_design_add, name="designer_design_add"),
    path('designer_design/edit/<design_id>', views.designer_design_edit, name="designer_design_edit"),
    path('designer_design/delete/<design_id>', views.designer_design_delete, name="designer_design_delete"),
    path('generate/', views.GeneratePdf.as_view(), name="generate"),
]