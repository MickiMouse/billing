(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-87d5cc82"],{"253d":function(t,e,i){},"3a2f":function(t,e,i){"use strict";i("60e8");var a=i("b64a"),s=i("163b"),n=i("c69d"),r=i("30d4"),o=i("b8d7"),c=i("98a1"),l=i("80d2"),d=i("d9bd");function h(t,e,i){return e in t?Object.defineProperty(t,e,{value:i,enumerable:!0,configurable:!0,writable:!0}):t[e]=i,t}e["a"]={name:"v-tooltip",mixins:[a["a"],s["a"],n["a"],r["a"],o["a"],c["a"]],props:{closeDelay:{type:[Number,String],default:200},debounce:{type:[Number,String],default:0},disabled:Boolean,fixed:{type:Boolean,default:!0},openDelay:{type:[Number,String],default:200},tag:{type:String,default:"span"},transition:String,zIndex:{default:null}},data:function(){return{calculatedMinWidth:0,closeDependents:!1}},computed:{calculatedLeft:function(){var t=this.dimensions,e=t.activator,i=t.content,a=!this.bottom&&!this.left&&!this.top&&!this.right,s=this.isAttached?e.offsetLeft:e.left,n=0;return this.top||this.bottom||a?n=s+e.width/2-i.width/2:(this.left||this.right)&&(n=s+(this.right?e.width:-i.width)+(this.right?10:-10)),this.nudgeLeft&&(n-=parseInt(this.nudgeLeft)),this.nudgeRight&&(n+=parseInt(this.nudgeRight)),this.calcXOverflow(n,this.dimensions.content.width)+"px"},calculatedTop:function(){var t=this.dimensions,e=t.activator,i=t.content,a=this.isAttached?e.offsetTop:e.top,s=0;return this.top||this.bottom?s=a+(this.bottom?e.height:-i.height)+(this.bottom?10:-10):(this.left||this.right)&&(s=a+e.height/2-i.height/2),this.nudgeTop&&(s-=parseInt(this.nudgeTop)),this.nudgeBottom&&(s+=parseInt(this.nudgeBottom)),this.calcYOverflow(s+this.pageYOffset)+"px"},classes:function(){return{"v-tooltip--top":this.top,"v-tooltip--right":this.right,"v-tooltip--bottom":this.bottom,"v-tooltip--left":this.left}},computedTransition:function(){return this.transition?this.transition:this.top?"slide-y-reverse-transition":this.right?"slide-x-transition":this.bottom?"slide-y-transition":this.left?"slide-x-reverse-transition":""},offsetY:function(){return this.top||this.bottom},offsetX:function(){return this.left||this.right},styles:function(){return{left:this.calculatedLeft,maxWidth:Object(l["d"])(this.maxWidth),minWidth:Object(l["d"])(this.minWidth),opacity:this.isActive?.9:0,top:this.calculatedTop,zIndex:this.zIndex||this.activeZIndex}}},beforeMount:function(){var t=this;this.$nextTick(function(){t.value&&t.callActivate()})},mounted:function(){"v-slot"===Object(l["n"])(this,"activator",!0)&&Object(d["a"])("v-tooltip's activator slot must be bound, try '<template #activator=\"data\"><v-btn v-on=\"data.on>'",this)},methods:{activate:function(){this.updateDimensions(),requestAnimationFrame(this.startTransition)},genActivator:function(){var t=this,e=this.disabled?{}:{mouseenter:function(e){t.getActivator(e),t.runDelay("open")},mouseleave:function(e){t.getActivator(e),t.runDelay("close")}};if("scoped"===Object(l["n"])(this,"activator")){var i=this.$scopedSlots.activator({on:e});return this.activatorNode=i,i}return this.$createElement("span",{on:e,ref:"activator"},this.$slots.activator)}},render:function(t){var e,i=t("div",this.setBackgroundColor(this.color,{staticClass:"v-tooltip__content",class:(e={},h(e,this.contentClass,!0),h(e,"menuable__content__active",this.isActive),h(e,"v-tooltip__content--fixed",this.activatorFixed),e),style:this.styles,attrs:this.getScopeIdAttrs(),directives:[{name:"show",value:this.isContentActive}],ref:"content"}),this.showLazyContent(this.$slots.default));return t(this.tag,{staticClass:"v-tooltip",class:this.classes},[t("transition",{props:{name:this.computedTransition}},[i]),this.genActivator()])}}},"3f19":function(t,e,i){"use strict";i.r(e);var a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-content",{attrs:{color:"primary"}},[i("v-snackbar",{attrs:{timeout:t.timeout,top:""},model:{value:t.snackbar,callback:function(e){t.snackbar=e},expression:"snackbar"}},[t._v("\n        "+t._s(t.text)+"\n        "),i("v-btn",{attrs:{flat:""},on:{click:function(e){t.snackbar=!1}}},[t._v("\n            Close\n        ")])],1),i("v-container",{attrs:{fluid:"",id:"main-container","grid-list-md":""}},[i("v-layout",{staticClass:"d-inline-block w-100 mb-5",attrs:{row:"",wrap:"","justify-center":""}},[i("v-card",[i("v-card-title",[t._v("\n                    Packages\n                    "),i("v-spacer"),i("v-text-field",{attrs:{"append-icon":"search",label:"Search","single-line":"","hide-details":""},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}})],1),i("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.packages,"items-per-page":5,loading:t.loading,search:t.search},scopedSlots:t._u([{key:"items",fn:function(e){return[i("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.pk))]),i("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.header))]),i("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.age_limit))]),i("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.tariff+t.$store.getters.currency))]),i("td",{staticClass:"text-xs-left"},[i("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(a){var s=a.on;return[i("v-btn",t._g({attrs:{color:"info",ripple:"",icon:"",small:"",dark:"",to:"/packages/"+e.item.pk+"/details/"}},s),[i("v-icon",{attrs:{small:""}},[t._v("info")])],1)]}}],null,!0)},[i("span",[t._v("Detail")])])],1)]}}])})],1)],1),i("v-dialog",{attrs:{"max-width":"600px"},scopedSlots:t._u([{key:"activator",fn:function(e){var a=e.on;return[t.$session.get("isSuperuser")?i("v-fab-transition",[i("v-btn",t._g({attrs:{color:"primary",dark:"",fixed:"",bottom:"",right:"",fab:""}},a),[i("v-icon",[t._v("add")])],1)],1):t._e()]}}]),model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[i("v-card",[i("v-card-title",[i("span",{staticClass:"headline"},[t._v("Package")])]),i("v-card-text",[i("v-container",{attrs:{"grid-list-md":""}},[i("v-form",{ref:"form"},[i("v-layout",{attrs:{wrap:""}},[i("v-flex",{attrs:{xs12:"",sm6:""}},[i("v-text-field",{attrs:{label:"Header*",rules:[t.rules.required]},model:{value:t.header,callback:function(e){t.header=e},expression:"header"}})],1),i("v-flex",{attrs:{xs12:"",sm6:""}},[i("v-text-field",{attrs:{label:"Tariff*",rules:[t.rules.required,t.rules.number,t.rules.counter]},model:{value:t.tariff,callback:function(e){t.tariff=e},expression:"tariff"}})],1)],1)],1)],1),i("small",[t._v("*indicates required field")])],1),i("v-card-actions",[i("v-spacer"),i("v-btn",{attrs:{color:"primary",text:""},on:{click:function(e){t.dialog=!1}}},[t._v("Close")]),i("v-btn",{attrs:{color:"primary",text:""},on:{click:t.submitPackageForm}},[t._v("Save")])],1)],1)],1)],1)],1)},s=[],n=i("bc3a"),r=i.n(n),o={name:"Packages",data:function(){return{headers:[{text:"Package ID",align:"left",value:"pk"},{text:"Header",value:"header"},{text:"Age limit",value:"age_limit"},{text:"Tariff",value:"tariff"},{text:"Action",value:"action",sortable:!1}],packages:[],loading:!0,snackbar:!1,dialog:!1,search:"",text:"Oops... Something went wrong",timeout:5e3,header:"",tariff:"",rules:{required:function(t){return!!t||"Required."},counter:function(t){return t<=2147483647||"Max 2147483647"},number:function(t){var e=/^\d+$/;return e.test(t)||"Invalid number."}}}},methods:{getData:function(){var t=this;r.a.get("".concat(this.$hostname,"/api/packages/")).then(function(e){console.log(e.data),200===e.status&&(t.packages=e.data,t.loading=!1)}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})},submitPackageForm:function(){var t=this;if(this.$refs.form.validate()){var e={crossdomain:!0,header:this.header,tariff:this.tariff};r.a.post("".concat(this.$hostname,"/api/packages/create/"),e).then(function(e){console.log(e.data),201===e.status&&(t.submitted=!0,t.dialog=!1,t.getData(),t.header="",t.tariff="",t.text="Package created!",t.snackbar=!0)}).catch(function(e){t.text="Connection error",t.snackbar=!0})}else this.text="Fill the form correctly",this.snackbar=!0}},beforeCreate:function(){this.$session.exists()||this.$router.push("/")},mounted:function(){this.getData()}},c=o,l=i("2877"),d=i("6544"),h=i.n(d),u=i("8336"),f=i("b0af"),m=i("99d9"),v=i("12b2"),p=i("a523"),g=i("549c"),b=i("8fea"),_=i("169a"),S=i("0789"),x=i("0e8f"),y=i("4bd4"),k=i("132d"),C=i("a722"),w=i("2db4"),$=i("9910"),z=i("2677"),A=i("3a2f"),I=Object(l["a"])(c,a,s,!1,null,"72d09310",null);e["default"]=I.exports;h()(I,{VBtn:u["a"],VCard:f["a"],VCardActions:m["a"],VCardText:m["b"],VCardTitle:v["a"],VContainer:p["a"],VContent:g["a"],VDataTable:b["a"],VDialog:_["a"],VFabTransition:S["b"],VFlex:x["a"],VForm:y["a"],VIcon:k["a"],VLayout:C["a"],VSnackbar:w["a"],VSpacer:$["a"],VTextField:z["a"],VTooltip:A["a"]})},"4c34":function(t,e,i){},"60e8":function(t,e,i){},"99d9":function(t,e,i){"use strict";var a=i("80d2"),s=i("b0af"),n=(i("253d"),i("4c34"),i("23bf")),r=i("58df"),o=Object(r["a"])(n["a"]).extend({name:"v-responsive",props:{aspectRatio:[String,Number]},computed:{computedAspectRatio:function(){return Number(this.aspectRatio)},aspectStyle:function(){return this.computedAspectRatio?{paddingBottom:1/this.computedAspectRatio*100+"%"}:void 0},__cachedSizer:function(){return this.aspectStyle?this.$createElement("div",{style:this.aspectStyle,staticClass:"v-responsive__sizer"}):[]}},methods:{genContent:function(){return this.$createElement("div",{staticClass:"v-responsive__content"},this.$slots.default)}},render:function(t){return t("div",{staticClass:"v-responsive",style:this.measurableStyles,on:this.$listeners},[this.__cachedSizer,this.genContent()])}}),c=o,l=i("d9bd"),d=c.extend({name:"v-img",props:{alt:String,contain:Boolean,src:{type:[String,Object],default:""},gradient:String,lazySrc:String,srcset:String,sizes:String,position:{type:String,default:"center center"},transition:{type:[Boolean,String],default:"fade-transition"}},data:function(){return{currentSrc:"",image:null,isLoading:!0,calculatedAspectRatio:void 0}},computed:{computedAspectRatio:function(){return this.normalisedSrc.aspect},normalisedSrc:function(){return"string"===typeof this.src?{src:this.src,srcset:this.srcset,lazySrc:this.lazySrc,aspect:Number(this.aspectRatio||this.calculatedAspectRatio)}:{src:this.src.src,srcset:this.srcset||this.src.srcset,lazySrc:this.lazySrc||this.src.lazySrc,aspect:Number(this.aspectRatio||this.src.aspect||this.calculatedAspectRatio)}},__cachedImage:function(){if(!this.normalisedSrc.src&&!this.normalisedSrc.lazySrc)return[];var t=[],e=this.isLoading?this.normalisedSrc.lazySrc:this.currentSrc;this.gradient&&t.push("linear-gradient("+this.gradient+")"),e&&t.push('url("'+e+'")');var i=this.$createElement("div",{staticClass:"v-image__image",class:{"v-image__image--preload":this.isLoading,"v-image__image--contain":this.contain,"v-image__image--cover":!this.contain},style:{backgroundImage:t.join(", "),backgroundPosition:this.position},key:+this.isLoading});return this.transition?this.$createElement("transition",{attrs:{name:this.transition,mode:"in-out"}},[i]):i}},watch:{src:function(){this.isLoading?this.loadImage():this.init()},"$vuetify.breakpoint.width":"getSrc"},mounted:function(){this.init()},methods:{init:function(){if(this.normalisedSrc.lazySrc){var t=new Image;t.src=this.normalisedSrc.lazySrc,this.pollForSize(t,null)}this.normalisedSrc.src&&this.loadImage()},onLoad:function(){this.getSrc(),this.isLoading=!1,this.$emit("load",this.src)},onError:function(){Object(l["a"])("Image load failed\n\nsrc: "+this.normalisedSrc.src,this),this.$emit("error",this.src)},getSrc:function(){this.image&&(this.currentSrc=this.image.currentSrc||this.image.src)},loadImage:function(){var t=this,e=new Image;this.image=e,e.onload=function(){e.decode?e.decode().catch(function(e){Object(l["c"])("Failed to decode image, trying to render anyway\n\nsrc: "+t.normalisedSrc.src+(e.message?"\nOriginal error: "+e.message:""),t)}).then(t.onLoad):t.onLoad()},e.onerror=this.onError,e.src=this.normalisedSrc.src,this.sizes&&(e.sizes=this.sizes),this.normalisedSrc.srcset&&(e.srcset=this.normalisedSrc.srcset),this.aspectRatio||this.pollForSize(e),this.getSrc()},pollForSize:function(t){var e=this,i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:100,a=function a(){var s=t.naturalHeight,n=t.naturalWidth;s||n?e.calculatedAspectRatio=n/s:null!=i&&setTimeout(a,i)};a()},__genPlaceholder:function(){if(this.$slots.placeholder){var t=this.isLoading?[this.$createElement("div",{staticClass:"v-image__placeholder"},this.$slots.placeholder)]:[];return this.transition?this.$createElement("transition",{attrs:{name:this.transition}},t):t[0]}}},render:function(t){var e=c.options.render.call(this,t);return e.data.staticClass+=" v-image",e.data.attrs={role:this.alt?"img":void 0,"aria-label":this.alt},e.children=[this.__cachedSizer,this.__cachedImage,this.__genPlaceholder(),this.genContent()],t(e.tag,e.data,e.children)}}),h=d.extend({name:"v-card-media",mounted:function(){Object(l["d"])("v-card-media",this.src?"v-img":"v-responsive",this)}}),u=i("12b2");i.d(e,"a",function(){return f}),i.d(e,"b",function(){return m});var f=Object(a["g"])("v-card__actions"),m=Object(a["g"])("v-card__text");s["a"],u["a"]}}]);
//# sourceMappingURL=chunk-87d5cc82.851fed0b.js.map