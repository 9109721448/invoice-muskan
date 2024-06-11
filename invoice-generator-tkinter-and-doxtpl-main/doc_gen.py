from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")

invoice_list = [[2, "bar", 0.5, 1],
                [1, "cement", 5, 5],
                [2, "bricks", 2, 4]]


doc.render({"name":"john", 
            "phone":"555-55555",
            "invoice_list": invoice_list,
            "subtotal":10,
            "salestax":"10%",
            "total":9})
doc.save("new_invoice.pdf")

