



// const FoodItem = {

//     return("
//     <div class="container flex-column">
//         <h3 class="text-center h3 fw-bold mt-5 p-4">Food Menu</h3>
//         {% for type in food %}
//         <div class="d-flex justify-content-between border-bottom border-dark m-3 p-3">
//             <p scope="col" class="fst-italic">{{type.name}}</p>
//             {% if session['user'] %}
//             <button class="btn btn-sm btn-outline-dark mx-3" class="" href="/delete/{{type.id}}" role="button">Delete</button>
//             {% endif %}
//         </div>
//         {% for item in type.item%}
//         <table class="border w-50 mt-2 tableitem">
//             <tr>
//                         <td class="me-auto p-2" scope="col">{{item.name}}</td>
//                         <td class="float-end">
//                         {% if session['user'] %}
//                         <!-- <span class="d-flex" role="group"> -->
//                             <a class="btn btn-sm btn-outline-dark mx-3" href="/delete/{{item.id}}" role="button">Delete</a>
//                             <button class="btn btn-sm btn-outline-dark" onclick="editButton('{{item.id}}')">Edit</button>
//                         <!-- </span> -->
//                         {% endif %}
//                     </td>
//                     <td class="p-2 fw-lighter">{{item.description}}..................... ${{item.price}}</td>
//                 </tr>
//                 {% if session['user'] %}
//                 <div class="edit-form" id="{{item.id}}">
//                     <form class="cols-lg-auto g-3 edit-form w-25 mx-auto" action='/edit/item/{{item.id}}'
//                         method="post">
//                         <div class="d-flex-col">
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='name'>Name:</label>
//                                 <input class="col-12" type="text" name='name' value="{{item.name}}">
//                             </div>
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='price'>Price:</label>
//                                 <input class="col-12" type="number" name='price' value="{{item.price}}">
//                             </div>
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='description'>Description:
//                                     (optional)</label>
//                                 <input class="col-12" type="number" name='description' value="{{item.description}}">
//                             </div>
//                             <div class="d-grid justify-content-center">
//                                 <button class="btn btn-outline-dark mt-2">Update</button>
//                             </div>
//                         </div>
//                     </form>
//                     {% endif %}
//             </table>
//             {% endfor %}
//         {% endfor %}
//     </div>

//     // <!-- VIEW DRINK MENU********************************* -->

//     <div class="mt-3 flex-row mb-1">
//         <h3 class="text-center h3 fw-bold mt-5">Drink Menu</h3>
//         {% for type in drinks %}
//         <div class="d-inline p-2 align-items-center flex-fill class">
//             <h6>{{type.name}}</h6>
//             {% for drink in type.drink %}
//             <table class="table table-borderless class-body">
//                 <tr>
//                     <thead>{{drink.name}}<br>{{drink.description}}</thead>
//                     <thead></thead>
//                 </tr>
//                 <tr>
//                     <tbody>
//                         <td>12oz ..................... ${{drink.small}}</td>
//                         <td>16oz ..................... ${{drink.medium}}</td>
//                         <td>20oz ..................... ${{drink.large}}</td>
//                     </tbody>
//                     {% if session['user'] %}
//                     <div class="col btn-group-sm mt-2 d-flex justify-content-center" role="group">
//                         <a class="btn btn-outline-dark mx-3" href="/delete/{{drink.id}}" role="button">Delete</a>
//                         <button class="btn btn-outline-dark mx-3" onclick="editButton('{{drink.id}}')">Edit</button>
//                     </div>
//                 </tr>
//                 <div class="edit-form" id="{{drink.id}}">
//                     <form class="cols-lg-auto g-3 edit-form w-50 mx-auto" action='/edit/drink/{{drink.id}}'
//                         method="post">
//                         <div class="d-flex-col">
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='name'>Name:</label>
//                                 <input class="col-12" type="text" name='name' value="{{drink.name}}">
//                             </div>
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='small'>12oz Price:</label>
//                                 <input class="col-12" type="number" name='small' value="{{drink.small}}">
//                             </div>
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='medium'>16oz Price:</label>
//                                 <input class="col-12" type="number" name='medium' value="{{drink.medium}}">
//                             </div>
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='large'>20oz Price:</label>
//                                 <input class="col-12" type="number" name='large' value="{{drink.large}}">
//                             </div>
//                             <div class="p-2">
//                                 <label class="col-sm-2 col-form-label-sm fs-6" for='description'>Description:
//                                     (optional)</label>
//                                 <input class="col-12" type="number" name='description' value="{{drink.description}}">
//                             </div>
//                             <div class="d-grid justify-content-center">
//                                 <button class="btn btn-outline-dark mt-2">Update</button>
//                             </div>
//                         </div>
//                     </form>
//                     {% endif %}
//             </table>
//             {% endfor %}
//         </div>
//         {% endfor %}
//     </div>
// ")}
