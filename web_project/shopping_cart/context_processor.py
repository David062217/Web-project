def import_total_cart(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total = total + (float(value["value"])*value["quantity"])
    return {"import_total_cart": total}