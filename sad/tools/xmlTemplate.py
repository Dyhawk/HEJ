from django.http import HttpResponse
import os


xml_content = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ASYCUDA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    {content}
</ASYCUDA>'''

item_element ='''<Item>
		<Suppliers_link>
			<Suppliers_link_code>1</Suppliers_link_code>
		</Suppliers_link>
		<Packages>
			<Number_of_packages></Number_of_packages>
			<Marks1_of_packages>AS ADDR</Marks1_of_packages>
			<Marks2_of_packages/>
			<Kind_of_packages_code>PK</Kind_of_packages_code>
			<Kind_of_packages_name>PACKAGE</Kind_of_packages_name>
		</Packages>
		<Tarification>
			<Tarification_data/>
			<HScode>
				<Commodity_code>{tariff}</Commodity_code>
				<Precision_1>000</Precision_1>
				<Precision_2/>
				<Precision_3/>
				<Precision_4>{sku}</Precision_4>
			</HScode>
			<Preference_code/>
			<Extended_customs_procedure>7100</Extended_customs_procedure>
			<National_customs_procedure>000</National_customs_procedure>
			<Quota_code/>
			<Supplementary_unit>
				<Suppplementary_unit_quantity>{quantity}</Suppplementary_unit_quantity>
			</Supplementary_unit>
			<Item_price>{cost}</Item_price>
			<Valuation_method_code/>
			<Attached_doc_item/>
			<A.I._code/>
		</Tarification>
		<Goods_description>
			<Country_of_origin_code>{country}</Country_of_origin_code>
			<Country_of_origin_region/>
			<Commercial_Description>{description}</Commercial_Description>
		</Goods_description>
		<Previous_doc>
			<Summary_declaration>{AWB}</Summary_declaration>
			<Summary_declaration_sl/>
			<Previous_document_reference/>
			<Previous_warehouse_code/>
		</Previous_doc>
		<Licence_number/>
		<Free_text_1/>
		<Free_text_2/>
		<Taxation>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
			<Taxation_line>
				<Duty_tax_Type_of_calculation/>
			</Taxation_line>
		</Taxation>
		<Valuation_item>
			<Weight_itm>
				<Gross_weight_itm>{weight}</Gross_weight_itm>
				<Net_weight_itm>{weight}</Net_weight_itm>
			</Weight_itm>
			<Item_Invoice>
				<Amount_foreign_currency>{cost}</Amount_foreign_currency>
				<Currency_code>USD</Currency_code>
				<Currency_name/>
				<Currency_rate>2.7169</Currency_rate>
			</Item_Invoice>
			<item_external_freight>
				<Currency_code/>
			</item_external_freight>
			<item_internal_freight>
				<Currency_code/>
			</item_internal_freight>
			<item_insurance>
				<Currency_code/>
			</item_insurance>
			<item_other_cost>
				<Currency_code/>
			</item_other_cost>
			<item_deduction>
				<Currency_code/>
			</item_deduction>
			<Market_valuer>
				<Currency_code/>
				<Basis_description/>
			</Market_valuer>
		</Valuation_item>
	</Item>
'''

def create_items(itemList):
    content = ''
    for item in itemList:
        content += item_element.format(
        sku = item.sku,
        description = item.description,
        tariff = item.tariff,
        country = item.country,
        quantity = item.quantity,
        cost = item.cost,
        weight = item.weight,
        AWB = item.awb
        )
    return content

def new_xml(itemList, name):
    data = {}
    count = 1
    for f in itemList:
        filename = str(name)+"-"+str(count)+".xml"
        # output_file = open(filename, 'w')
        render_content = xml_content.format(content = create_items(f))
        response = HttpResponse(render_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        count += 1
        #data.update({filename: response})
    return response
