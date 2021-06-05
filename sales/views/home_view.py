from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from sales.models import *
from sales.forms import SalesSearchForm
import pandas as pd


def home_view(request):
    sales_df = None
    positions_df = None
    form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)

        # qs = query set
        # qsf = query set filtered
        # qs = Sale.objects.all()// qsf converted to sale_qs
        sale_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs) > 0:
            #for showing in dataframe
            sales_df = pd.DataFrame(sale_qs.values())
            positions_data = []
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                    }
                    positions_data.append(obj)
            positions_df = pd.DataFrame(positions_data)
            print('positions_df')
            print(positions_df)

            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()


        else:
            print("No data")

        # obj = Sale.objects.get(id=2)
        # print(qsf)
        # print(obj)
        # print(qsf.values())
        # print((qsf.values_list()))

        # print('**********')
        # df1 = pd.DataFrame(qsf.values())
        # print(df1)
        # print('**********')

        # print('**********')
        # df2 = pd.DataFrame(qsf.values_list())
        # print(df2)
        # print('**********')

    context = {
        'form': form,
        'sales_df': sales_df,
        'positions_df': positions_df,
    }
    return render(request, 'sales/home.html', context)


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'


class SaleDetailView(DeleteView):
    model = Sale
    template_name = 'sales/detail.html'
