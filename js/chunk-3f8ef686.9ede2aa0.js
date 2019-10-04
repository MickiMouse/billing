(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3f8ef686"],{1696:function(t,a,e){},"4b26":function(t,a,e){"use strict";e.r(a);var n=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-content",{attrs:{color:"primary"}},[e("v-snackbar",{attrs:{timeout:t.timeout,top:""},model:{value:t.snackbar,callback:function(a){t.snackbar=a},expression:"snackbar"}},[t._v("\n        "+t._s(t.text)+"\n        "),e("v-btn",{attrs:{flat:""},on:{click:function(a){t.snackbar=!1}}},[t._v("\n            Close\n        ")])],1),e("v-container",{attrs:{fluid:"",id:"main-container","grid-list-md":""}},[this.$session.get("isSuperuser")?e("v-dialog",{attrs:{"max-width":"290"},model:{value:t.addManyCards,callback:function(a){t.addManyCards=a},expression:"addManyCards"}},[e("v-form",{ref:"form"},[e("v-card",[e("v-card-text",[e("v-row",[e("v-col",{staticClass:"px-4"},[e("v-range-slider",{staticClass:"align-center",attrs:{max:t.max,min:t.min,"hide-details":""},scopedSlots:t._u([{key:"prepend",fn:function(){return[e("v-text-field",{staticClass:"mt-0 pt-0",staticStyle:{width:"60px"},attrs:{rules:[t.rules.counter,t.rules.number],"hide-details":"","single-line":"",type:"number"},model:{value:t.range[0],callback:function(a){t.$set(t.range,0,a)},expression:"range[0]"}})]},proxy:!0},{key:"append",fn:function(){return[e("v-text-field",{staticClass:"mt-0 pt-0",staticStyle:{width:"60px"},attrs:{rules:[t.rules.counter,t.rules.number],"hide-details":"","single-line":"",type:"number"},model:{value:t.range[1],callback:function(a){t.$set(t.range,1,a)},expression:"range[1]"}})]},proxy:!0}],null,!1,3487234398),model:{value:t.range,callback:function(a){t.range=a},expression:"range"}})],1)],1)],1),e("v-card-actions",[e("v-spacer"),e("v-btn",{attrs:{outline:"",small:"",color:"error"},on:{click:function(a){a.stopPropagation(),t.addManyCards=!1}}},[t._v("Close")]),e("v-btn",{attrs:{small:"",text:"",color:"primary"},on:{click:function(a){return a.stopPropagation(),t.createManyCards(a)}}},[t._v("Add")])],1)],1)],1)],1):t._e(),e("v-layout",{staticClass:"d-inline-block w-100 mb-5",attrs:{row:"",wrap:"","justify-center":""}},[e("v-card",[e("v-card-title",[t._v("\n                    Cards\n                    "),e("v-spacer"),e("v-text-field",{attrs:{"append-icon":"search",label:"Search","single-line":"","hide-details":""},model:{value:t.search,callback:function(a){t.search=a},expression:"search"}})],1),e("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.cards,"items-per-page":5,loading:t.loading,search:t.search},scopedSlots:t._u([{key:"items",fn:function(a){return[e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.pk))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.label))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.created_at))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.last_change))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.expired_date))]),e("td",{staticClass:"text-xs-left"},[t._v(t._s(a.item.status))]),e("td",{staticClass:"text-xs-left"},[e("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(n){var s=n.on;return[e("v-btn",t._g({attrs:{color:"info",ripple:"",icon:"",small:"",dark:"",to:"/cards/"+a.item.pk+"/details/"}},s),[e("v-icon",{attrs:{small:""}},[t._v("info")])],1)]}}],null,!0)},[e("span",[t._v("Detail")])])],1)]}}])})],1)],1),this.$session.get("isSuperuser")?e("v-speed-dial",{attrs:{color:"primary",dark:"",fixed:"",bottom:"",right:"",fab:"",direction:"top","open-on-hover":t.hover,transition:"slide-y-transition"},scopedSlots:t._u([{key:"activator",fn:function(){return[e("v-btn",{attrs:{color:"primary",dark:"",fab:""},model:{value:t.fab,callback:function(a){t.fab=a},expression:"fab"}},[t.fab?e("v-icon",[t._v("close")]):e("v-icon",[t._v("library_add")])],1)]},proxy:!0}],null,!1,2663113574),model:{value:t.fab,callback:function(a){t.fab=a},expression:"fab"}},[e("v-btn",{attrs:{fab:"",dark:"",small:"",color:"primary darken-1"},on:{click:t.createCard}},[e("v-icon",[t._v("add")])],1),e("v-btn",{attrs:{fab:"",dark:"",small:"",color:"primary darken-1"},on:{click:function(a){a.stopPropagation(),t.addManyCards=!0}}},[e("v-icon",[t._v("playlist_add")])],1)],1):t._e()],1)],1)},s=[],i=e("bc3a"),r=e.n(i),o={name:"Cards",data:function(){return{headers:[{text:"Card ID",align:"left",value:"pk"},{text:"Card Label",value:"label"},{text:"Issued",value:"created_at"},{text:"Edited",value:"last_change"},{text:"Expired",value:"expired_date"},{text:"Status",value:"status"},{text:"Action",value:"action",sortable:!1}],cards:[],loading:!0,snackbar:!1,search:"",fab:!1,hover:!0,text:"Oops... Something went wrong",timeout:5e3,addManyCards:!1,min:0,range:[],rules:{counter:function(t){return t<=2147483647&&t>=1||"Min 1 and Max 2147483647"},number:function(t){var a=/^\d+$/;return a.test(t)||"Invalid number."}}}},computed:{max:function(){return this.min+99}},methods:{getData:function(){var t=this;r.a.get("".concat(this.$hostname,"/api/cards/")).then(function(a){console.log(a.data),200===a.status&&(t.cards=a.data,t.loading=!1)}).catch(function(a){t.text="Connection error",console.log(a),t.snackbar=!0}),this.getRange()},createCard:function(){var t=this;r.a.post("".concat(this.$hostname,"/api/cards/create/")).then(function(a){console.log(a.data),201===a.status&&(t.getData(),t.text="Card created!",t.snackbar=!0)}).catch(function(a){t.text="Connection error",t.snackbar=!0})},createManyCards:function(){var t=this;this.$refs.form.validate()?(this.loading=!0,r.a.post("".concat(this.$hostname,"/api/cards/create/range/"),{start:this.range[0],stop:this.range[1]}).then(function(a){console.log(a.data),201===a.status&&(t.getData(),t.text="Cards from ".concat(t.range[0]," to ").concat(t.range[1]," were created!"),t.snackbar=!0,t.addManyCards=!1)}).catch(function(a){t.addManyCards=!1,t.text="Connection error",t.snackbar=!0})):(this.text="Fill the form correctly",this.snackbar=!0)},getRange:function(){var t=this;this.loading=!0,r.a.get("".concat(this.$hostname,"/api/cards/create/range/")).then(function(a){console.log(a.data),200===a.status&&(t.min=a.data.start,t.loading=!1,t.range=[t.min,t.min+10],t.rules.counter=function(a){return a<=t.min+99&&a>=t.min||"Min 1 and Max 2147483647"})}).catch(function(a){t.text="Connection error",console.log(a),t.snackbar=!0})}},beforeCreate:function(){this.$session.exists()||this.$router.push("/")},mounted:function(){this.getData()}},c=o,l=e("2877"),d=e("6544"),u=e.n(d),p=e("8336"),v=e("b0af"),f=e("99d9"),m=e("12b2"),b=e("a523"),h=e("549c"),g=e("8fea"),x=e("169a"),k=e("4bd4"),C=e("132d"),y=e("a722"),_=e("5963"),S=e("2db4"),V=e("9910"),w=(e("1696"),e("98a1")),$=e("c22b"),M=e("2b0e"),D=M["a"].extend({name:"transitionable",props:{mode:String,origin:String,transition:String}}),A=e("c584");function O(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}var T={name:"v-speed-dial",directives:{ClickOutside:A["a"]},mixins:[$["a"],w["a"],D],props:{direction:{type:String,default:"top",validator:function(t){return["top","right","bottom","left"].includes(t)}},openOnHover:Boolean,transition:{type:String,default:"scale-transition"}},computed:{classes:function(){return O({"v-speed-dial":!0,"v-speed-dial--top":this.top,"v-speed-dial--right":this.right,"v-speed-dial--bottom":this.bottom,"v-speed-dial--left":this.left,"v-speed-dial--absolute":this.absolute,"v-speed-dial--fixed":this.fixed},"v-speed-dial--direction-"+this.direction,!0)}},render:function(t){var a=this,e=[],n={class:this.classes,directives:[{name:"click-outside",value:function(){return a.isActive=!1}}],on:{click:function(){return a.isActive=!a.isActive}}};if(this.openOnHover&&(n.on.mouseenter=function(){return a.isActive=!0},n.on.mouseleave=function(){return a.isActive=!1}),this.isActive){var s=0;e=(this.$slots.default||[]).map(function(a,e){return a.tag&&"undefined"!==typeof a.componentOptions&&"v-btn"===a.componentOptions.Ctor.options.name?(s++,t("div",{style:{transitionDelay:.05*s+"s"},key:e},[a])):(a.key=e,a)})}var i=t("transition-group",{class:"v-speed-dial__list",props:{name:this.transition,mode:this.mode,origin:this.origin,tag:"div"}},e);return t("div",n,[this.$slots.activator,i])}},I=e("2677"),P=e("3a2f"),j=Object(l["a"])(c,n,s,!1,null,"705fbd4f",null);a["default"]=j.exports;u()(j,{VBtn:p["a"],VCard:v["a"],VCardActions:f["a"],VCardText:f["b"],VCardTitle:m["a"],VContainer:b["a"],VContent:h["a"],VDataTable:g["a"],VDialog:x["a"],VForm:k["a"],VIcon:C["a"],VLayout:y["a"],VRangeSlider:_["a"],VSnackbar:S["a"],VSpacer:V["a"],VSpeedDial:T,VTextField:I["a"],VTooltip:P["a"]})}}]);
//# sourceMappingURL=chunk-3f8ef686.9ede2aa0.js.map