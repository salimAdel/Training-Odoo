import json
from odoo import http
from odoo.http import request

class TestApi(http.Controller):

    @http.route("/api/v1/shipping/stores/get-all", methods=["GET"], type="http", auth="none", csrf=False)
    def stores_list(self):
        try:
            records = request.env['store_done'].sudo().search([])
            result = records.read(['id', 'name'])
            return request.make_json_response({
                'massage':"sucsses",
                'result':result
            } ,status = 200)
        except Exception as e:
            return request.make_json_response({
                'message': "something went wrong",
                'error': str(e)
            }, status=400)
        
    @http.route("/api/v1/shipping/stores/<int:id>", methods=["GET"], type="http", auth="none", csrf=False)
    def store_by_id(self, id):
        try:
            record = request.env['store_done'].sudo().browse(id)
            if not record.exists():
                return request.make_json_response({
                    'message': "record not found"
                }, status=404)

            result = record.read(['id', 'name']) 
            return request.make_json_response({
                'message': "success",
                'result': result[0] if result else {}
            }, status=200)
        except Exception as e:
            return request.make_json_response({
                'message': "something went wrong",
                'error': str(e)
            }, status=400)
        

    @http.route("/api/v1/shipping/stores",method=["POST"], type="json", auth="none",csrf=False)
    def create_store(self):
        try:
            arg = request.httprequest.data.decode()
            val = json.loads(arg)
            record = request.env['store_done'].sudo().create(val)
            result = record.read('id', 'name')
            return{
                "massage":"the store created succssfully",
            }
        except Exception as e:
            return request.make_json_response({
                'message': "something went wrong",
                'error': str(e)
            }, status=400)
        


    @http.route("/api/v1/shipping/stores/<int:id>",method = ["PUT"], type="json",auth="none",csrf=False)
    def edit_stoer(self,id):
        try:
            store = request.env['store_done'].sudo().browse(id)
            if not store.exists():
                return request.make_json_response({
                    'message': "record not found"
                }, status=404)
            
            arg = request.httprequest.data.decode()
            val = json.loads(arg)
            store.write(val)
            return{
                "massage":"the store Updated succssfully",
            }
        except Exception as e :
            return request.make_json_response({
                'message': "something went wrong",
                'error': str(e)
            }, status=400)
        



    @http.route("/api/v1/shipping/stores/<int:id>",method = ["DELETE"], type="http",auth="none",csrf=False)
    def delete_store(self,id):
        try:
            store = request.env['store_done'].sudo().browse(id)
            if not store.exists():
                return request.make_json_response({
                    'message': "record not found"
                }, status=404)

            store.unlink()
            return request.make_json_response({
                "message": "The store was deleted successfully"
            }, status=200)

        except Exception as e:
            return request.make_json_response({
                'message': "something went wrong",
                'error': str(e)
            }, status=400)
