prefix_filtering =  "Output guids as a python list for the following question: "
prefix_csv_description = "This file contains a list of elements of a under construction project. Columns in this table are" + \
   "status: element status" + \
   "floor: element floor" + \
    "type: element type (its class in IFC format)" + \
    "name: element name" + \
    "globalId: element global id or guid or id" + \
    "magnitude: deviation magnitude of the element. the more the worse" + \
    "approved: whether the element status is approved by quality assurance or not." + \
    "DO NO DO ANYTHING AND JUST WAIT FOR THE NEXT QUESTION"
suffix_data_type = "send me the results in JSON format,'echoedText' is your answer, field 'ids' is an array of guids"
suffix_guid_list = "PROVIDE THE LIST OF globalIds. RETURN EMPTY LIST IF THERE IS NO DATA"
suffix_plot_status = "Based on the 'status' use colors orange for deviated, gray for no data, red for missing and green for verified"
error_message = "Sorry, the free version does not allow me to process too many elements.\
                 This is just a demo! Are you trying to break me? :(\
                 Please buy my developers some coffee/beer if you really want me to answer these questions."

