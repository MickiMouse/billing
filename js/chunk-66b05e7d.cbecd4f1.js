(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-66b05e7d"],{"00da":function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-content",{attrs:{color:"primary"}},[a("v-container",{attrs:{fluid:"",id:"main-container","grid-list-md":"","fill-height":""}},[a("v-snackbar",{attrs:{timeout:t.timeout,top:""},model:{value:t.snackbar,callback:function(e){t.snackbar=e},expression:"snackbar"}},[t._v("\n            "+t._s(t.text)+"\n            "),a("v-btn",{attrs:{flat:""},on:{click:function(e){t.snackbar=!1}}},[t._v("\n                Close\n            ")])],1),a("v-layout",{attrs:{"justify-center":"",wrap:""}},[a("v-flex",{attrs:{sm8:"",xs12:""}},[a("v-card",{staticClass:"mx-auto",attrs:{loading:t.loading}},[a("v-list",{attrs:{"two-line":"",subheader:"",dense:""}},[a("v-subheader",[t._v("Details\n                            "),a("v-dialog",{attrs:{persistent:"","max-width":"290"},scopedSlots:t._u([{key:"activator",fn:function(e){var i=e.on;return[a("v-btn",t._g({staticClass:"ml-auto mr-0",attrs:{color:"error",small:"",icon:"",ripple:""}},i),[a("v-icon",{attrs:{small:""}},[t._v("delete")])],1)]}}]),model:{value:t.deletePackageDialog,callback:function(e){t.deletePackageDialog=e},expression:"deletePackageDialog"}},[a("v-card",[a("v-card-title",{staticClass:"headline"},[t._v("Lorem ipsum dolor sit.")]),a("v-card-text",[t._v("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius maiores odit quo sunt tenetur vitae?")]),a("v-card-actions",[a("v-spacer"),a("v-btn",{attrs:{small:"",color:"error"},on:{click:function(e){t.deletePackageDialog=!1}}},[t._v("Close")]),a("v-btn",{attrs:{outline:"",small:"",color:"error"},on:{click:t.deletePackage}},[t._v("Delete")])],1)],1)],1)],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("archive")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Header")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.header)+"\n                                ")])],1)],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("account_balance_wallet")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Tariff")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.tariff))])],1),a("v-list-tile-action",[a("v-dialog",{attrs:{persistent:"","max-width":"600px"},scopedSlots:t._u([{key:"activator",fn:function(e){var i=e.on;return[a("v-btn",t._g({attrs:{icon:"",ripple:""}},i),[a("v-icon",{attrs:{color:"grey lighten-1"}},[t._v("edit")])],1)]}}]),model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[a("v-card",[a("v-card-text",[a("v-container",{attrs:{"grid-list-md":""}},[a("v-layout",{attrs:{wrap:""}},[a("v-flex",{attrs:{xs12:""}},[a("v-form",{ref:"tariffForm"},[a("v-text-field",{attrs:{label:"Tariff",type:"number",required:"",rules:[t.rules.counterTariff,t.rules.number]},model:{value:t.newBalance,callback:function(e){t.newBalance=e},expression:"newBalance"}})],1)],1)],1)],1)],1),a("v-card-actions",[a("v-spacer"),a("v-btn",{attrs:{color:"primary",text:""},on:{click:function(e){t.dialog=!1}}},[t._v("Close")]),a("v-btn",{attrs:{color:"primary",text:""},on:{click:t.changeBalance}},[t._v("Save")])],1)],1)],1)],1)],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("tv_off")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Age limit")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.age_limit))])],1)],1),t.details.cards?a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("card_membership")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Total cards")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.cards.length))])],1)],1):t._e()],1)],1)],1),a("v-flex",{attrs:{sm4:"",xs12:""}},[a("v-card",{staticClass:"mb-3"},[a("v-card-title",[a("v-text-field",{attrs:{"append-icon":"search",label:"Search","single-line":"","hide-details":""},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}})],1)],1),a("v-card",{staticClass:"my-3"},[a("v-subheader",[t._v("Bouquets")]),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.bouquets,"items-per-page":"5",loading:t.loadingbouquets,search:t.search},scopedSlots:t._u([{key:"items",fn:function(e){return[a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.name))]),a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.age_limit))]),a("td",{staticClass:"text-xs-left no-wrap"},[a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(i){var s=i.on;return[a("v-btn",t._g({attrs:{color:"error",ripple:"",icon:"",small:"",dark:""},on:{click:function(a){return t.removeBouquet(e.item.number)}}},s),[a("v-icon",{attrs:{small:""}},[t._v("close")])],1)]}}],null,!0)},[a("span",[t._v("Remove")])])],1)]}}])})],1),a("v-card",{staticClass:"my-3"},[a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.availableBouquets,"items-per-page":"5",loading:t.loadingAvailableBouquets,search:t.search},scopedSlots:t._u([{key:"items",fn:function(e){return[a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.name))]),a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.age_limit))]),a("td",{staticClass:"text-xs-left no-wrap"},[a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(i){var s=i.on;return[a("v-btn",t._g({attrs:{color:"success",ripple:"",icon:"",small:"",dark:""},on:{click:function(a){return t.addBouquet(e.item.number)}}},s),[a("v-icon",{attrs:{small:""}},[t._v("add")])],1)]}}],null,!0)},[a("span",[t._v("Add")])])],1)]}}])})],1)],1)],1)],1)],1)},s=[],n=a("bc3a"),o=a.n(n),r={name:"bouquetsDetails",data:function(){return{snack:!1,snackColor:"",snackText:"",loading:!0,loadingbouquets:!0,loadingAvailableBouquets:!0,snackbar:!1,dialog:!1,search:"",text:"Oops... Something went wrong",timeout:5e3,details:{},deletePackageDialog:!1,newBalance:"",headers:[{text:"Header",align:"left",value:"name"},{text:"Age limit",align:"left",value:"age_limit"},{text:"Action",value:"action",sortable:!1}],bouquets:[],availableBouquets:[],rules:{counter:function(t){return t<=128||"Max 128"},counterTariff:function(t){return t<=2147483647||"Max 2147483647"},number:function(t){var e=/^\d+$/;return e.test(t)||"Invalid number."}}}},computed:{},methods:{getData:function(){var t=this;this.loadingbouquets=!0,o.a.get("".concat(this.$hostname,"/api/packages/").concat(this.$route.params.id,"/")).then(function(e){200===e.status&&(console.log(e.data),t.details=e.data,t.bouquets=t.details.bouquets,t.newBalance=t.details.tariff,t.loadingbouquets=!1,console.log(e.data,t.bouquets))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0}),this.loadingAvailableBouquets=!0,o.a.get("".concat(this.$hostname,"/api/bouquets/").concat(this.$route.params.id,"/")).then(function(e){200===e.status&&(t.availableBouquets=e.data,t.loadingAvailableBouquets=!1,console.log(e.data))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})},addBouquet:function(t){var e=this;o.a.put("".concat(this.$hostname,"/api/packages/edit/bouquets/").concat(this.$route.params.id,"/"),{bouquet:t}).then(function(t){200===t.status&&(console.log(t.data),e.getData())}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0})},removeBouquet:function(t){var e=this;o.a.put("".concat(this.$hostname,"/api/packages/delete/bouquets/").concat(this.$route.params.id,"/"),{bouquet:t}).then(function(t){200===t.status&&(console.log(t.data),e.getData())}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0})},deletePackage:function(){var t=this;o.a.delete("".concat(this.$hostname,"/api/packages/delete/").concat(this.$route.params.id,"/")).then(function(e){204===e.status&&(console.log(e.data),t.$router.push("/packages"))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})},changeBalance:function(){var t=this;if(this.$refs.tariffForm.validate()){this.loading=!0;var e={tariff:this.newBalance};o.a.put("".concat(this.$hostname,"/api/packages/edit/tariff/").concat(this.$route.params.id,"/"),e).then(function(e){200===e.status&&(t.details.tariff=e.data.tariff,t.newBalance=t.details.tariff,t.loading=!1,t.dialog=!1,t.text="Tariff changed!",t.snackbar=!0)}).catch(function(e){400===e.response.status?(t.text="Balance too low",t.snackbar=!0):(t.text="Connection error",console.log(e),t.snackbar=!0)})}else this.text="Fill the form correctly",this.snackbar=!0}},beforeCreate:function(){this.$session.exists()||this.$router.push("/")},mounted:function(){this.getData()}},c=r,l=a("2877"),d=a("6544"),u=a.n(d),h=a("8336"),v=a("b0af"),f=a("99d9"),m=a("12b2"),g=a("a523"),p=a("549c"),b=a("8fea"),_=a("169a"),x=a("0e8f"),S=a("4bd4"),y=a("132d"),k=a("a722"),C=a("8860"),w=a("ba95"),$=a("40fe"),A=a("c954"),B=a("5d23"),q=a("2db4"),T=a("9910"),L=a("e0c7"),z=a("2677"),V=a("3a2f"),D=Object(l["a"])(c,i,s,!1,null,"27de9153",null);e["default"]=D.exports;u()(D,{VBtn:h["a"],VCard:v["a"],VCardActions:f["a"],VCardText:f["b"],VCardTitle:m["a"],VContainer:g["a"],VContent:p["a"],VDataTable:b["a"],VDialog:_["a"],VFlex:x["a"],VForm:S["a"],VIcon:y["a"],VLayout:k["a"],VList:C["a"],VListTile:w["a"],VListTileAction:$["a"],VListTileAvatar:A["a"],VListTileContent:B["a"],VListTileSubTitle:B["b"],VListTileTitle:B["c"],VSnackbar:q["a"],VSpacer:T["a"],VSubheader:L["a"],VTextField:z["a"],VTooltip:V["a"]})},"253d":function(t,e,a){},"3a2f":function(t,e,a){"use strict";a("60e8");var i=a("b64a"),s=a("163b"),n=a("c69d"),o=a("30d4"),r=a("b8d7"),c=a("98a1"),l=a("80d2"),d=a("d9bd");function u(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}e["a"]={name:"v-tooltip",mixins:[i["a"],s["a"],n["a"],o["a"],r["a"],c["a"]],props:{closeDelay:{type:[Number,String],default:200},debounce:{type:[Number,String],default:0},disabled:Boolean,fixed:{type:Boolean,default:!0},openDelay:{type:[Number,String],default:200},tag:{type:String,default:"span"},transition:String,zIndex:{default:null}},data:function(){return{calculatedMinWidth:0,closeDependents:!1}},computed:{calculatedLeft:function(){var t=this.dimensions,e=t.activator,a=t.content,i=!this.bottom&&!this.left&&!this.top&&!this.right,s=this.isAttached?e.offsetLeft:e.left,n=0;return this.top||this.bottom||i?n=s+e.width/2-a.width/2:(this.left||this.right)&&(n=s+(this.right?e.width:-a.width)+(this.right?10:-10)),this.nudgeLeft&&(n-=parseInt(this.nudgeLeft)),this.nudgeRight&&(n+=parseInt(this.nudgeRight)),this.calcXOverflow(n,this.dimensions.content.width)+"px"},calculatedTop:function(){var t=this.dimensions,e=t.activator,a=t.content,i=this.isAttached?e.offsetTop:e.top,s=0;return this.top||this.bottom?s=i+(this.bottom?e.height:-a.height)+(this.bottom?10:-10):(this.left||this.right)&&(s=i+e.height/2-a.height/2),this.nudgeTop&&(s-=parseInt(this.nudgeTop)),this.nudgeBottom&&(s+=parseInt(this.nudgeBottom)),this.calcYOverflow(s+this.pageYOffset)+"px"},classes:function(){return{"v-tooltip--top":this.top,"v-tooltip--right":this.right,"v-tooltip--bottom":this.bottom,"v-tooltip--left":this.left}},computedTransition:function(){return this.transition?this.transition:this.top?"slide-y-reverse-transition":this.right?"slide-x-transition":this.bottom?"slide-y-transition":this.left?"slide-x-reverse-transition":""},offsetY:function(){return this.top||this.bottom},offsetX:function(){return this.left||this.right},styles:function(){return{left:this.calculatedLeft,maxWidth:Object(l["d"])(this.maxWidth),minWidth:Object(l["d"])(this.minWidth),opacity:this.isActive?.9:0,top:this.calculatedTop,zIndex:this.zIndex||this.activeZIndex}}},beforeMount:function(){var t=this;this.$nextTick(function(){t.value&&t.callActivate()})},mounted:function(){"v-slot"===Object(l["n"])(this,"activator",!0)&&Object(d["a"])("v-tooltip's activator slot must be bound, try '<template #activator=\"data\"><v-btn v-on=\"data.on>'",this)},methods:{activate:function(){this.updateDimensions(),requestAnimationFrame(this.startTransition)},genActivator:function(){var t=this,e=this.disabled?{}:{mouseenter:function(e){t.getActivator(e),t.runDelay("open")},mouseleave:function(e){t.getActivator(e),t.runDelay("close")}};if("scoped"===Object(l["n"])(this,"activator")){var a=this.$scopedSlots.activator({on:e});return this.activatorNode=a,a}return this.$createElement("span",{on:e,ref:"activator"},this.$slots.activator)}},render:function(t){var e,a=t("div",this.setBackgroundColor(this.color,{staticClass:"v-tooltip__content",class:(e={},u(e,this.contentClass,!0),u(e,"menuable__content__active",this.isActive),u(e,"v-tooltip__content--fixed",this.activatorFixed),e),style:this.styles,attrs:this.getScopeIdAttrs(),directives:[{name:"show",value:this.isContentActive}],ref:"content"}),this.showLazyContent(this.$slots.default));return t(this.tag,{staticClass:"v-tooltip",class:this.classes},[t("transition",{props:{name:this.computedTransition}},[a]),this.genActivator()])}}},"4c34":function(t,e,a){},"60e8":function(t,e,a){},"99d9":function(t,e,a){"use strict";var i=a("80d2"),s=a("b0af"),n=(a("253d"),a("4c34"),a("23bf")),o=a("58df"),r=Object(o["a"])(n["a"]).extend({name:"v-responsive",props:{aspectRatio:[String,Number]},computed:{computedAspectRatio:function(){return Number(this.aspectRatio)},aspectStyle:function(){return this.computedAspectRatio?{paddingBottom:1/this.computedAspectRatio*100+"%"}:void 0},__cachedSizer:function(){return this.aspectStyle?this.$createElement("div",{style:this.aspectStyle,staticClass:"v-responsive__sizer"}):[]}},methods:{genContent:function(){return this.$createElement("div",{staticClass:"v-responsive__content"},this.$slots.default)}},render:function(t){return t("div",{staticClass:"v-responsive",style:this.measurableStyles,on:this.$listeners},[this.__cachedSizer,this.genContent()])}}),c=r,l=a("d9bd"),d=c.extend({name:"v-img",props:{alt:String,contain:Boolean,src:{type:[String,Object],default:""},gradient:String,lazySrc:String,srcset:String,sizes:String,position:{type:String,default:"center center"},transition:{type:[Boolean,String],default:"fade-transition"}},data:function(){return{currentSrc:"",image:null,isLoading:!0,calculatedAspectRatio:void 0}},computed:{computedAspectRatio:function(){return this.normalisedSrc.aspect},normalisedSrc:function(){return"string"===typeof this.src?{src:this.src,srcset:this.srcset,lazySrc:this.lazySrc,aspect:Number(this.aspectRatio||this.calculatedAspectRatio)}:{src:this.src.src,srcset:this.srcset||this.src.srcset,lazySrc:this.lazySrc||this.src.lazySrc,aspect:Number(this.aspectRatio||this.src.aspect||this.calculatedAspectRatio)}},__cachedImage:function(){if(!this.normalisedSrc.src&&!this.normalisedSrc.lazySrc)return[];var t=[],e=this.isLoading?this.normalisedSrc.lazySrc:this.currentSrc;this.gradient&&t.push("linear-gradient("+this.gradient+")"),e&&t.push('url("'+e+'")');var a=this.$createElement("div",{staticClass:"v-image__image",class:{"v-image__image--preload":this.isLoading,"v-image__image--contain":this.contain,"v-image__image--cover":!this.contain},style:{backgroundImage:t.join(", "),backgroundPosition:this.position},key:+this.isLoading});return this.transition?this.$createElement("transition",{attrs:{name:this.transition,mode:"in-out"}},[a]):a}},watch:{src:function(){this.isLoading?this.loadImage():this.init()},"$vuetify.breakpoint.width":"getSrc"},mounted:function(){this.init()},methods:{init:function(){if(this.normalisedSrc.lazySrc){var t=new Image;t.src=this.normalisedSrc.lazySrc,this.pollForSize(t,null)}this.normalisedSrc.src&&this.loadImage()},onLoad:function(){this.getSrc(),this.isLoading=!1,this.$emit("load",this.src)},onError:function(){Object(l["a"])("Image load failed\n\nsrc: "+this.normalisedSrc.src,this),this.$emit("error",this.src)},getSrc:function(){this.image&&(this.currentSrc=this.image.currentSrc||this.image.src)},loadImage:function(){var t=this,e=new Image;this.image=e,e.onload=function(){e.decode?e.decode().catch(function(e){Object(l["c"])("Failed to decode image, trying to render anyway\n\nsrc: "+t.normalisedSrc.src+(e.message?"\nOriginal error: "+e.message:""),t)}).then(t.onLoad):t.onLoad()},e.onerror=this.onError,e.src=this.normalisedSrc.src,this.sizes&&(e.sizes=this.sizes),this.normalisedSrc.srcset&&(e.srcset=this.normalisedSrc.srcset),this.aspectRatio||this.pollForSize(e),this.getSrc()},pollForSize:function(t){var e=this,a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:100,i=function i(){var s=t.naturalHeight,n=t.naturalWidth;s||n?e.calculatedAspectRatio=n/s:null!=a&&setTimeout(i,a)};i()},__genPlaceholder:function(){if(this.$slots.placeholder){var t=this.isLoading?[this.$createElement("div",{staticClass:"v-image__placeholder"},this.$slots.placeholder)]:[];return this.transition?this.$createElement("transition",{attrs:{name:this.transition}},t):t[0]}}},render:function(t){var e=c.options.render.call(this,t);return e.data.staticClass+=" v-image",e.data.attrs={role:this.alt?"img":void 0,"aria-label":this.alt},e.children=[this.__cachedSizer,this.__cachedImage,this.__genPlaceholder(),this.genContent()],t(e.tag,e.data,e.children)}}),u=d.extend({name:"v-card-media",mounted:function(){Object(l["d"])("v-card-media",this.src?"v-img":"v-responsive",this)}}),h=a("12b2");a.d(e,"a",function(){return v}),a.d(e,"b",function(){return f});var v=Object(i["g"])("v-card__actions"),f=Object(i["g"])("v-card__text");s["a"],h["a"]}}]);
//# sourceMappingURL=chunk-66b05e7d.cbecd4f1.js.map