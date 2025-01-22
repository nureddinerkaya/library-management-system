from sanic import Sanic, Blueprint,response

from backend.app.copies.CopiesServices import CopiesServices

# CopiesServices blueprint
copies_blueprint = Blueprint("copies", url_prefix="/copies")

@copies_blueprint.route("/createcopy",methods=["POST"])
async def create_copy(request):
    return  await CopiesServices.add_copy(request)

@copies_blueprint.route("/Getbycopyid",methods=["GET"])
async def get_copy(request):
    """Handles retrieving a specific copy."""
    return await CopiesServices.view_copies_by_id(request)

@copies_blueprint.route("/getallcopies",methods=["GET"])
async def list_all_copies(request):
    """Handles listing all copies."""
    return await CopiesServices.view_copies(request)

@copies_blueprint.route("/getbyprintno",methods=["GET"])
async def list_copies_byprintno(request):

    return await CopiesServices.view_copies_by_print_no(request)



@copies_blueprint.route("/getbylocation",methods=["GET"])
async def list_copies_bylocation(request):

    return await CopiesServices.view_copies_by_location(request)



@copies_blueprint.route("/getbyavailability",methods=["GET"])
async def list_copies_byavailability(request):
    #/getbyavailability?availability=Yes
    return await CopiesServices.view_copies_by_availability(request)


@copies_blueprint.route("/getbyadditiondate",methods=["GET"])
async def list_copies_byadditiondate(request):
    """Handles listing all copies."""
    return await CopiesServices.view_copies_by_additiondate(request)


@copies_blueprint.route("/updatecopybyid",methods=["PUT"])
async def update_copy(request):
    """Handles updating a specific copy."""
    return  await CopiesServices.update_copy(request)

@copies_blueprint.route("/deletecopybyid",methods=["DELETE"])
async def delete_copy(request):
    """Handles deleting a specific copy."""
    return  await CopiesServices.delete_copy(request)
