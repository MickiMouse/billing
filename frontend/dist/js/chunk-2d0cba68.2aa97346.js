(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0cba68"],{"4b26":function(t,a,e){"use strict";e.r(a);var s=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-content",{attrs:{color:"primary"}},[e("v-snackbar",{attrs:{timeout:t.timeout,top:""},model:{value:t.snackbar,callback:function(a){t.snackbar=a},expression:"snackbar"}},[t._v("\n        "+t._s(t.text)+"\n        "),e("v-btn",{attrs:{flat:""},on:{click:function(a){t.snackbar=!1}}},[t._v("\n            Close\n        ")])],1),e("v-container",{attrs:{fluid:"",id:"main-container","grid-list-md":""}},[e("v-layout",{staticClass:"d-inline-block w-100",attrs:{row:"",wrap:"","justify-center":""}},[e("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.cards,"items-per-page":5,loading:t.loading},scopedSlots:t._u([{key:"items",fn:function(a){return[e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.pk))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.label))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.created_at))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.last_change))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.expired_date))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.status))]),e("td",{staticClass:"text-xs-left"},[e("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(s){var n=s.on;return[e("v-btn",t._g({attrs:{color:"info",fab:"",small:"",dark:"",to:"/cards/"+a.item.pk+"/details/"}},n),[e("v-icon",[t._v("info")])],1)]}}],null,!0)},[e("span",[t._v("Detail")])])],1)]}}])})],1),e("v-fab-transition",[e("v-btn",t._g({attrs:{color:"primary",dark:"",fixed:"",bottom:"",right:"",fab:""}},t.on),[e("v-icon",[t._v("add")])],1)],1)],1)],1)},n=[],i=e("bc3a"),o=e.n(i),r={name:"Cards",data:function(){return{headers:[{text:"Card ID",align:"left",value:"pk"},{text:"Card Label",value:"label"},{text:"Issued",value:"created_at"},{text:"Edited",value:"last_change"},{text:"Expired",value:"expired_date"},{text:"Status",value:"status"},{text:"Action",value:"action",sortable:!1}],cards:[],loading:!0,snackbar:!1,text:"Oops... Something went wrong",timeout:5e3}},methods:{getData:function(){var t=this;o.a.get("".concat(this.$hostname,"/api/cards/")).then(function(a){console.log(a.data),200===a.status&&(t.cards=a.data,t.loading=!1)}).catch(function(a){t.text="Connection error",console.log(a),t.snackbar=!0})}},beforeCreate:function(){this.$session.exists()||this.$router.push("/")},mounted:function(){this.getData()}},c=r,l=e("2877"),d=e("6544"),u=e.n(d),v=e("8336"),f=e("a523"),b=e("549c"),x=e("8fea"),_=e("0789"),m=e("132d"),p=e("a722"),k=e("2db4"),h=e("3a2f"),g=Object(l["a"])(c,s,n,!1,null,"0deb6c72",null);a["default"]=g.exports;u()(g,{VBtn:v["a"],VContainer:f["a"],VContent:b["a"],VDataTable:x["a"],VFabTransition:_["b"],VIcon:m["a"],VLayout:p["a"],VSnackbar:k["a"],VTooltip:h["a"]})}}]);
//# sourceMappingURL=chunk-2d0cba68.2aa97346.js.map