(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6b69d58f"],{"253d":function(t,e,a){},"2e29":function(t,e,a){},"3a2f":function(t,e,a){"use strict";a("60e8");var s=a("b64a"),i=a("163b"),n=a("c69d"),o=a("30d4"),r=a("b8d7"),c=a("98a1"),l=a("80d2"),d=a("d9bd");function u(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}e["a"]={name:"v-tooltip",mixins:[s["a"],i["a"],n["a"],o["a"],r["a"],c["a"]],props:{closeDelay:{type:[Number,String],default:200},debounce:{type:[Number,String],default:0},disabled:Boolean,fixed:{type:Boolean,default:!0},openDelay:{type:[Number,String],default:200},tag:{type:String,default:"span"},transition:String,zIndex:{default:null}},data:function(){return{calculatedMinWidth:0,closeDependents:!1}},computed:{calculatedLeft:function(){var t=this.dimensions,e=t.activator,a=t.content,s=!this.bottom&&!this.left&&!this.top&&!this.right,i=this.isAttached?e.offsetLeft:e.left,n=0;return this.top||this.bottom||s?n=i+e.width/2-a.width/2:(this.left||this.right)&&(n=i+(this.right?e.width:-a.width)+(this.right?10:-10)),this.nudgeLeft&&(n-=parseInt(this.nudgeLeft)),this.nudgeRight&&(n+=parseInt(this.nudgeRight)),this.calcXOverflow(n,this.dimensions.content.width)+"px"},calculatedTop:function(){var t=this.dimensions,e=t.activator,a=t.content,s=this.isAttached?e.offsetTop:e.top,i=0;return this.top||this.bottom?i=s+(this.bottom?e.height:-a.height)+(this.bottom?10:-10):(this.left||this.right)&&(i=s+e.height/2-a.height/2),this.nudgeTop&&(i-=parseInt(this.nudgeTop)),this.nudgeBottom&&(i+=parseInt(this.nudgeBottom)),this.calcYOverflow(i+this.pageYOffset)+"px"},classes:function(){return{"v-tooltip--top":this.top,"v-tooltip--right":this.right,"v-tooltip--bottom":this.bottom,"v-tooltip--left":this.left}},computedTransition:function(){return this.transition?this.transition:this.top?"slide-y-reverse-transition":this.right?"slide-x-transition":this.bottom?"slide-y-transition":this.left?"slide-x-reverse-transition":""},offsetY:function(){return this.top||this.bottom},offsetX:function(){return this.left||this.right},styles:function(){return{left:this.calculatedLeft,maxWidth:Object(l["d"])(this.maxWidth),minWidth:Object(l["d"])(this.minWidth),opacity:this.isActive?.9:0,top:this.calculatedTop,zIndex:this.zIndex||this.activeZIndex}}},beforeMount:function(){var t=this;this.$nextTick(function(){t.value&&t.callActivate()})},mounted:function(){"v-slot"===Object(l["n"])(this,"activator",!0)&&Object(d["a"])("v-tooltip's activator slot must be bound, try '<template #activator=\"data\"><v-btn v-on=\"data.on>'",this)},methods:{activate:function(){this.updateDimensions(),requestAnimationFrame(this.startTransition)},genActivator:function(){var t=this,e=this.disabled?{}:{mouseenter:function(e){t.getActivator(e),t.runDelay("open")},mouseleave:function(e){t.getActivator(e),t.runDelay("close")}};if("scoped"===Object(l["n"])(this,"activator")){var a=this.$scopedSlots.activator({on:e});return this.activatorNode=a,a}return this.$createElement("span",{on:e,ref:"activator"},this.$slots.activator)}},render:function(t){var e,a=t("div",this.setBackgroundColor(this.color,{staticClass:"v-tooltip__content",class:(e={},u(e,this.contentClass,!0),u(e,"menuable__content__active",this.isActive),u(e,"v-tooltip__content--fixed",this.activatorFixed),e),style:this.styles,attrs:this.getScopeIdAttrs(),directives:[{name:"show",value:this.isContentActive}],ref:"content"}),this.showLazyContent(this.$slots.default));return t(this.tag,{staticClass:"v-tooltip",class:this.classes},[t("transition",{props:{name:this.computedTransition}},[a]),this.genActivator()])}}},"4c34":function(t,e,a){},"60e8":function(t,e,a){},"99d9":function(t,e,a){"use strict";var s=a("80d2"),i=a("b0af"),n=(a("253d"),a("4c34"),a("23bf")),o=a("58df"),r=Object(o["a"])(n["a"]).extend({name:"v-responsive",props:{aspectRatio:[String,Number]},computed:{computedAspectRatio:function(){return Number(this.aspectRatio)},aspectStyle:function(){return this.computedAspectRatio?{paddingBottom:1/this.computedAspectRatio*100+"%"}:void 0},__cachedSizer:function(){return this.aspectStyle?this.$createElement("div",{style:this.aspectStyle,staticClass:"v-responsive__sizer"}):[]}},methods:{genContent:function(){return this.$createElement("div",{staticClass:"v-responsive__content"},this.$slots.default)}},render:function(t){return t("div",{staticClass:"v-responsive",style:this.measurableStyles,on:this.$listeners},[this.__cachedSizer,this.genContent()])}}),c=r,l=a("d9bd"),d=c.extend({name:"v-img",props:{alt:String,contain:Boolean,src:{type:[String,Object],default:""},gradient:String,lazySrc:String,srcset:String,sizes:String,position:{type:String,default:"center center"},transition:{type:[Boolean,String],default:"fade-transition"}},data:function(){return{currentSrc:"",image:null,isLoading:!0,calculatedAspectRatio:void 0}},computed:{computedAspectRatio:function(){return this.normalisedSrc.aspect},normalisedSrc:function(){return"string"===typeof this.src?{src:this.src,srcset:this.srcset,lazySrc:this.lazySrc,aspect:Number(this.aspectRatio||this.calculatedAspectRatio)}:{src:this.src.src,srcset:this.srcset||this.src.srcset,lazySrc:this.lazySrc||this.src.lazySrc,aspect:Number(this.aspectRatio||this.src.aspect||this.calculatedAspectRatio)}},__cachedImage:function(){if(!this.normalisedSrc.src&&!this.normalisedSrc.lazySrc)return[];var t=[],e=this.isLoading?this.normalisedSrc.lazySrc:this.currentSrc;this.gradient&&t.push("linear-gradient("+this.gradient+")"),e&&t.push('url("'+e+'")');var a=this.$createElement("div",{staticClass:"v-image__image",class:{"v-image__image--preload":this.isLoading,"v-image__image--contain":this.contain,"v-image__image--cover":!this.contain},style:{backgroundImage:t.join(", "),backgroundPosition:this.position},key:+this.isLoading});return this.transition?this.$createElement("transition",{attrs:{name:this.transition,mode:"in-out"}},[a]):a}},watch:{src:function(){this.isLoading?this.loadImage():this.init()},"$vuetify.breakpoint.width":"getSrc"},mounted:function(){this.init()},methods:{init:function(){if(this.normalisedSrc.lazySrc){var t=new Image;t.src=this.normalisedSrc.lazySrc,this.pollForSize(t,null)}this.normalisedSrc.src&&this.loadImage()},onLoad:function(){this.getSrc(),this.isLoading=!1,this.$emit("load",this.src)},onError:function(){Object(l["a"])("Image load failed\n\nsrc: "+this.normalisedSrc.src,this),this.$emit("error",this.src)},getSrc:function(){this.image&&(this.currentSrc=this.image.currentSrc||this.image.src)},loadImage:function(){var t=this,e=new Image;this.image=e,e.onload=function(){e.decode?e.decode().catch(function(e){Object(l["c"])("Failed to decode image, trying to render anyway\n\nsrc: "+t.normalisedSrc.src+(e.message?"\nOriginal error: "+e.message:""),t)}).then(t.onLoad):t.onLoad()},e.onerror=this.onError,e.src=this.normalisedSrc.src,this.sizes&&(e.sizes=this.sizes),this.normalisedSrc.srcset&&(e.srcset=this.normalisedSrc.srcset),this.aspectRatio||this.pollForSize(e),this.getSrc()},pollForSize:function(t){var e=this,a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:100,s=function s(){var i=t.naturalHeight,n=t.naturalWidth;i||n?e.calculatedAspectRatio=n/i:null!=a&&setTimeout(s,a)};s()},__genPlaceholder:function(){if(this.$slots.placeholder){var t=this.isLoading?[this.$createElement("div",{staticClass:"v-image__placeholder"},this.$slots.placeholder)]:[];return this.transition?this.$createElement("transition",{attrs:{name:this.transition}},t):t[0]}}},render:function(t){var e=c.options.render.call(this,t);return e.data.staticClass+=" v-image",e.data.attrs={role:this.alt?"img":void 0,"aria-label":this.alt},e.children=[this.__cachedSizer,this.__cachedImage,this.__genPlaceholder(),this.genContent()],t(e.tag,e.data,e.children)}}),u=d.extend({name:"v-card-media",mounted:function(){Object(l["d"])("v-card-media",this.src?"v-img":"v-responsive",this)}}),h=a("12b2");a.d(e,"a",function(){return v}),a.d(e,"b",function(){return p});var v=Object(s["g"])("v-card__actions"),p=Object(s["g"])("v-card__text");i["a"],h["a"]},b06d:function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-content",{attrs:{color:"primary"}},[a("v-container",{attrs:{fluid:"",id:"main-container","grid-list-md":"","fill-height":""}},[a("v-snackbar",{attrs:{timeout:t.timeout,top:""},model:{value:t.snackbar,callback:function(e){t.snackbar=e},expression:"snackbar"}},[t._v("\n            "+t._s(t.text)+"\n            "),a("v-btn",{attrs:{flat:""},on:{click:function(e){t.snackbar=!1}}},[t._v("\n                Close\n            ")])],1),a("v-layout",{attrs:{"justify-center":"",wrap:""}},[a("v-flex",{attrs:{sm8:"",xs12:""}},[a("v-card",{staticClass:"mx-auto",attrs:{loading:t.loading}},[a("v-list",{attrs:{"two-line":"",subheader:"",dense:""}},[a("v-subheader",[t._v("Details\n                            "),"Active"!==this.details.status?a("v-dialog",{attrs:{persistent:"","max-width":"290"},scopedSlots:t._u([{key:"activator",fn:function(e){var s=e.on;return[a("v-btn",t._g({staticClass:"ml-auto mr-0",attrs:{color:"error",small:"",icon:"",ripple:""}},s),[a("v-icon",{attrs:{small:""}},[t._v("delete")])],1)]}}],null,!1,2751930783),model:{value:t.deleteDialog,callback:function(e){t.deleteDialog=e},expression:"deleteDialog"}},[a("v-card",[a("v-card-title",{staticClass:"headline"},[t._v("Lorem ipsum dolor sit.")]),a("v-card-text",[t._v("Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consectetur\n                                        adipisicing elit. Quam, similique.\n                                    ")]),a("v-card-actions",[a("v-spacer"),a("v-btn",{attrs:{small:"",color:"error"},on:{click:function(e){t.deleteDialog=!1}}},[t._v("Close")]),a("v-btn",{attrs:{outline:"",small:"",color:"error"},on:{click:t.deleteSubscriber}},[t._v("Delete")])],1)],1)],1):t._e()],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("folder_special")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Label")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.label)+"\n                                ")])],1)],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("playlist_add_check")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Status")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.status))])],1),a("v-list-tile-avatar",[a("v-switch",{attrs:{disabled:"Active"!==t.details.status&&"Suspend"!==t.details.status},on:{change:t.updateStatus},model:{value:t.status,callback:function(e){t.status=e},expression:"status"}})],1)],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("account_balance_wallet")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Price")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.price))])],1)],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("event_busy")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Expired date")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.expired_date))])],1),t.$store.getters.isPREPAYMENT&&"Inactive"!==t.details.status?a("div",{staticClass:"d-flex align-center justify-center",class:{"d-none":t.$vuetify.breakpoint.xs,"":t.$vuetify.breakpoint.smAndUp}},[a("v-form",{ref:"form"},[a("v-text-field",{staticClass:"mr-2 ml-auto",attrs:{label:"Periods",type:"number",rules:[t.rules.counter,t.rules.number]},model:{value:t.numOfPeriods,callback:function(e){t.numOfPeriods=e},expression:"numOfPeriods"}})],1),a("v-btn",{staticClass:"ml-auto",attrs:{color:"pink",dark:"",small:"",ripple:"",icon:""},on:{click:t.updateCardPeriod}},[a("v-icon",{attrs:{small:""}},[t._v("autorenew")])],1)],1):t._e()],1),t.$store.getters.isPREPAYMENT&&"Inactive"!==t.details.status?a("v-list-tile",{class:{"":t.$vuetify.breakpoint.xs,"d-none":t.$vuetify.breakpoint.smAndUp},attrs:{avatar:""}},[a("div",{staticClass:"d-flex align-center justify-center"},[a("v-form",{ref:"form"},[a("v-text-field",{staticClass:"mr-2 ml-auto",attrs:{label:"Periods",type:"number",rules:[t.rules.counter,t.rules.number]},model:{value:t.numOfPeriods,callback:function(e){t.numOfPeriods=e},expression:"numOfPeriods"}})],1),a("v-btn",{staticClass:"ml-auto",attrs:{color:"pink",dark:"",small:"",ripple:"",icon:""},on:{click:t.updateCardPeriod}},[a("v-icon",{attrs:{small:""}},[t._v("autorenew")])],1)],1)]):t._e(),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("event_note")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Last change")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.last_change))])],1)],1),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("insert_invitation")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Created at")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.created_at))])],1)],1),t.details.subscriber?a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("person")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Subscriber")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.subscriber.email))])],1),a("v-list-tile-avatar",[a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(e){var s=e.on;return[a("v-btn",t._g({attrs:{to:"/subscribers/"+t.details.subscriber.pk+"/details/",color:"info",ripple:"",icon:"",small:"",dark:""}},s),[a("v-icon",{attrs:{small:""}},[t._v("info")])],1)]}}],null,!1,1497581810)},[a("span",[t._v("Detail")])])],1)],1):t._e(),a("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[a("v-list-tile-avatar",[a("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("people")])],1),a("v-list-tile-content",[a("v-list-tile-title",[t._v("Reseller")]),a("v-list-tile-sub-title",[t._v(t._s(t.details.reseller.email))])],1),a("v-list-tile-avatar",[a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(e){var s=e.on;return[a("v-btn",t._g({attrs:{to:"/resellers/"+t.details.reseller.pk+"/details/",color:"info",ripple:"",icon:"",small:"",dark:""}},s),[a("v-icon",{attrs:{small:""}},[t._v("info")])],1)]}}])},[a("span",[t._v("Detail")])])],1)],1)],1)],1),t.$session.get("isSuperuser")?a("v-card",{staticClass:"mt-3"},[a("v-card-title",[a("v-text-field",{attrs:{"append-icon":"search",label:"Search","single-line":"","hide-details":""},model:{value:t.searchLogs,callback:function(e){t.searchLogs=e},expression:"searchLogs"}})],1)],1):t._e(),t.$session.get("isSuperuser")?a("v-card",{staticClass:"my-3"},[a("v-subheader",[t._v("Logs")]),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headersLogs,items:t.details.logs,"items-per-page":"5",search:t.searchLogs},scopedSlots:t._u([{key:"items",fn:function(e){return[a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.date))]),a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.log))])]}}],null,!1,1050048653)})],1):t._e()],1),a("v-flex",{attrs:{xs12:"",sm4:""}},[a("v-card",{staticClass:"mb-3"},[a("v-card-title",[a("v-text-field",{attrs:{"append-icon":"search",label:"Search","single-line":"","hide-details":""},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}})],1)],1),a("v-card",{staticClass:"my-3"},[a("v-subheader",[t._v("Packages")]),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.packages,"items-per-page":"5",loading:t.loadingPackages,search:t.search},scopedSlots:t._u([{key:"items",fn:function(e){return[a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.header))]),a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.tariff))]),a("td",{staticClass:"text-xs-left no-wrap"},[a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(s){var i=s.on;return[a("v-btn",t._g({attrs:{to:"/packages/"+e.item.pk+"/details/",color:"info",ripple:"",icon:"",small:"",dark:""}},i),[a("v-icon",{attrs:{small:""}},[t._v("info")])],1)]}}],null,!0)},[a("span",[t._v("Detail")])]),a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(s){var i=s.on;return[a("v-btn",t._g({attrs:{color:"error",ripple:"",icon:"",small:"",dark:""},on:{click:function(a){return t.removeCard(e.item.pk)}}},i),[a("v-icon",{attrs:{small:""}},[t._v("close")])],1)]}}],null,!0)},[a("span",[t._v("Remove now")])]),a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(s){var i=s.on;return[a("v-btn",t._g({attrs:{color:"error darken-1",ripple:"",icon:"",small:"",dark:""},on:{click:function(a){return t.removeCardLater(e.item.pk)}}},i),[a("v-icon",{attrs:{small:""}},[t._v("alarm_off")])],1)]}}],null,!0)},[a("span",[t._v("Remove later")])])],1)]}}])})],1),a("v-card",{staticClass:"my-3"},[a("v-subheader",[t._v("Available packages")]),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.aviablePackages,"items-per-page":"5",loading:t.loadingAviablePackages,search:t.search},scopedSlots:t._u([{key:"items",fn:function(e){return[a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.header))]),a("td",{staticClass:"text-xs-left no-wrap"},[t._v(t._s(e.item.tariff))]),a("td",{staticClass:"text-xs-left no-wrap"},[a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(s){var i=s.on;return[a("v-btn",t._g({attrs:{to:"/packages/"+e.item.pk+"/details/",color:"info",ripple:"",icon:"",small:"",dark:""}},i),[a("v-icon",{attrs:{small:""}},[t._v("info")])],1)]}}],null,!0)},[a("span",[t._v("Detail")])]),a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(s){var i=s.on;return[a("v-btn",t._g({attrs:{color:"success",ripple:"",icon:"",small:"",dark:""},on:{click:function(a){return t.addPackage(e.item.pk)}}},i),[a("v-icon",{attrs:{small:""}},[t._v("add")])],1)]}}],null,!0)},[a("span",[t._v("Add now")])]),a("v-tooltip",{attrs:{bottom:""},scopedSlots:t._u([{key:"activator",fn:function(s){var i=s.on;return[a("v-btn",t._g({attrs:{color:"success darken-1",ripple:"",icon:"",small:"",dark:""},on:{click:function(a){return t.addPackageLater(e.item.pk)}}},i),[a("v-icon",{attrs:{small:""}},[t._v("add_alarm")])],1)]}}],null,!0)},[a("span",[t._v("Add later")])])],1)]}}])})],1)],1)],1)],1)],1)},i=[],n=(a("c5f6"),a("04ff"),a("bc3a")),o=a.n(n),r={name:"CardsDetails",data:function(){return{snack:!1,snackColor:"",snackText:"",loading:!0,loadingPackages:!0,loadingAviablePackages:!0,snackbar:!1,dialog:!1,search:"",searchLogs:"",text:"Oops... Something went wrong",timeout:5e3,newBalance:"",numOfPeriods:1,details:{address:"",balance:0,cards:Array(0),email:"",first_name:"",id:0,last_name:"",reseller:0,telephone:""},headers:[{text:"Header",align:"left",value:"header"},{text:"Tariff",align:"left",value:"tariff"},{text:"Action",value:"action",sortable:!1}],headersLogs:[{text:"Date",value:"date"},{text:"Header",align:"left",value:"log"}],packages:[],aviablePackages:[],rules:{counter:function(t){return t<=2147483647&&t>=1||"Min 1 and Max 2147483647"},number:function(t){var e=/^\d+$/;return e.test(t)||"Invalid number."}},deleteDialog:!1}},computed:{status:function(){return"Active"===this.details.status}},methods:{getData:function(){var t=this;this.loadingPackages=!0,o.a.get("".concat(this.$hostname,"/api/cards/").concat(this.$route.params.id,"/")).then(function(e){200===e.status&&(console.log(e.data),t.details=e.data,t.packages=t.details.packages,t.newBalance=t.details.balance,t.loadingPackages=!1,console.log(e.data))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0}),this.loadingAviablePackages=!0,o.a.get("".concat(this.$hostname,"/api/packages-filter/").concat(this.$route.params.id,"/")).then(function(e){200===e.status&&(t.aviablePackages=e.data,t.loadingAviablePackages=!1,console.log(e.data))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})},updateStatus:function(){var t=this;o.a.put("".concat(this.$hostname,"/api/cards/edit/status/").concat(this.$route.params.id,"/")).then(function(e){200===e.status&&(t.getData(),t.text="Status changed!",t.snackbar=!0)}).catch(function(e){t.details.status=!t.details.status,t.text="Connection error",console.log(e),t.snackbar=!0})},updateCardPeriod:function(){var t=this;this.$refs.form.validate()?(this.loading=!0,o.a.put("".concat(this.$hostname,"/api/cards/edit/expired/").concat(this.$route.params.id,"/"),{period:Number.parseInt(this.numOfPeriods)}).then(function(e){200===e.status&&(t.getData(),t.text="Period changed!",t.snackbar=!0)}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})):(this.text="Fill the form correctly",this.snackbar=!0)},addPackage:function(t){var e=this;o.a.put("".concat(this.$hostname,"/api/cards/edit/package/").concat(this.$route.params.id,"/"),{package:t}).then(function(t){200===t.status&&(console.log(t.data),e.getData())}).catch(function(t){400===t.response.status?(e.details.status=!e.details.status,e.text="The subscriber does not have enough funds",console.log(t),e.snackbar=!0):(e.details.status=!e.details.status,e.text="Connection error",console.log(t),e.snackbar=!0)})},addPackageLater:function(t){var e=this;o.a.post("".concat(this.$hostname,"/api/cards/delayed-add/package/").concat(this.$route.params.id,"/"),{package:t}).then(function(t){200===t.status&&(console.log(t.data),e.getData())}).catch(function(t){400===t.response.status?(e.details.status=!e.details.status,e.text="The subscriber does not have enough funds",console.log(t),e.snackbar=!0):(e.details.status=!e.details.status,e.text="Connection error",console.log(t),e.snackbar=!0)})},removeCard:function(t){var e=this;o.a.put("".concat(this.$hostname,"/api/cards/delete/package/").concat(this.$route.params.id,"/"),{package:t}).then(function(t){200===t.status&&(console.log(t.data),e.getData())}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0})},removeCardLater:function(t){var e=this;o.a.post("".concat(this.$hostname,"/api/cards/delayed-remove/package/").concat(this.$route.params.id,"/"),{package:t}).then(function(t){200===t.status&&(console.log(t.data),e.getData())}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0})},deleteSubscriber:function(){var t=this;o.a.delete("".concat(this.$hostname,"/api/cards/delete/").concat(this.$route.params.id,"/")).then(function(e){204===e.status&&(console.log(e.data),t.$router.push("/cards"))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})}},beforeCreate:function(){this.$session.exists()||this.$router.push("/")},mounted:function(){this.getData()}},c=r,l=a("2877"),d=a("6544"),u=a.n(d),h=a("8336"),v=a("b0af"),p=a("99d9"),m=a("12b2"),f=a("a523"),g=a("549c"),b=a("8fea"),_=a("169a"),k=a("0e8f"),x=a("4bd4"),S=a("132d"),y=a("a722"),C=a("8860"),w=a("ba95"),$=a("c954"),L=a("5d23"),A=a("2db4"),P=a("9910"),D=a("e0c7"),T=a("b73d"),O=a("2677"),z=a("3a2f"),V=Object(l["a"])(c,s,i,!1,null,"03e1e644",null);e["default"]=V.exports;u()(V,{VBtn:h["a"],VCard:v["a"],VCardActions:p["a"],VCardText:p["b"],VCardTitle:m["a"],VContainer:f["a"],VContent:g["a"],VDataTable:b["a"],VDialog:_["a"],VFlex:k["a"],VForm:x["a"],VIcon:S["a"],VLayout:y["a"],VList:C["a"],VListTile:w["a"],VListTileAvatar:$["a"],VListTileContent:L["a"],VListTileSubTitle:L["b"],VListTileTitle:L["c"],VSnackbar:A["a"],VSpacer:P["a"],VSubheader:D["a"],VSwitch:T["a"],VTextField:O["a"],VTooltip:z["a"]})},b73d:function(t,e,a){"use strict";a("94a7"),a("2e29");var s=a("5368"),i=a("c341"),n=a("0789"),o=a("490a"),r=a("80d2"),c=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var a=arguments[e];for(var s in a)Object.prototype.hasOwnProperty.call(a,s)&&(t[s]=a[s])}return t};e["a"]={name:"v-switch",directives:{Touch:i["a"]},mixins:[s["a"]],props:{loading:{type:[Boolean,String],default:!1}},computed:{classes:function(){return{"v-input--selection-controls v-input--switch":!0}},switchData:function(){return this.setTextColor(this.loading?void 0:this.computedColor,{class:this.themeClasses})}},methods:{genDefaultSlot:function(){return[this.genSwitch(),this.genLabel()]},genSwitch:function(){return this.$createElement("div",{staticClass:"v-input--selection-controls__input"},[this.genInput("checkbox",this.$attrs),this.genRipple(this.setTextColor(this.computedColor,{directives:[{name:"touch",value:{left:this.onSwipeLeft,right:this.onSwipeRight}}]})),this.$createElement("div",c({staticClass:"v-input--switch__track"},this.switchData)),this.$createElement("div",c({staticClass:"v-input--switch__thumb"},this.switchData),[this.genProgress()])])},genProgress:function(){return this.$createElement(n["b"],{},[!1===this.loading?null:this.$slots.progress||this.$createElement(o["a"],{props:{color:!0===this.loading||""===this.loading?this.color||"primary":this.loading,size:16,width:2,indeterminate:!0}})])},onSwipeLeft:function(){this.isActive&&this.onChange()},onSwipeRight:function(){this.isActive||this.onChange()},onKeydown:function(t){(t.keyCode===r["r"].left&&this.isActive||t.keyCode===r["r"].right&&!this.isActive)&&this.onChange()}}}}}]);
//# sourceMappingURL=chunk-6b69d58f.597f49c2.js.map