(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-44814fb8"],{"0d81":function(t,e,i){},"12b2":function(t,e,i){"use strict";var a=i("2b0e");e["a"]=a["a"].extend({name:"v-card-title",functional:!0,props:{primaryTitle:Boolean},render:function(t,e){var i=e.data,a=e.props,s=e.children;return i.staticClass=("v-card__title "+(i.staticClass||"")).trim(),a.primaryTitle&&(i.staticClass+=" v-card__title--primary"),t("div",i,s)}})},"253d":function(t,e,i){},3828:function(t,e,i){"use strict";i.r(e);var a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-content",{attrs:{color:"primary"}},[i("v-container",{attrs:{fluid:"",id:"main-container","grid-list-md":"","fill-height":""}},[i("v-snackbar",{attrs:{timeout:t.timeout,top:""},model:{value:t.snackbar,callback:function(e){t.snackbar=e},expression:"snackbar"}},[t._v("\n            "+t._s(t.text)+"\n            "),i("v-btn",{attrs:{flat:""},on:{click:function(e){t.snackbar=!1}}},[t._v("\n                Close\n            ")])],1),i("v-layout",{attrs:{"justify-center":"",wrap:""}},[i("v-flex",{attrs:{sm8:"",xs12:""}},[i("v-card",{staticClass:"mx-auto",attrs:{loading:t.loading}},[i("v-form",{ref:"form",on:{submit:function(t){t.preventDefault()}}},[i("v-list",{attrs:{"two-line":"",subheader:"",dense:""}},[i("v-subheader",[t._v("Details\n                                "),i("v-dialog",{attrs:{persistent:"","max-width":"290"},scopedSlots:t._u([{key:"activator",fn:function(e){var a=e.on;return[i("v-btn",t._g({staticClass:"ml-auto mr-0",attrs:{color:"error",small:"",icon:"",ripple:""}},a),[i("v-icon",{attrs:{small:""}},[t._v("delete")])],1)]}}]),model:{value:t.deleteDialog,callback:function(e){t.deleteDialog=e},expression:"deleteDialog"}},[i("v-card",[i("v-card-title",{staticClass:"headline"},[t._v("Lorem ipsum dolor sit.")]),i("v-card-text",[t._v("Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet,\n                                            consectetur adipisicing elit. Quam, similique.\n                                        ")]),i("v-card-actions",[i("v-spacer"),i("v-btn",{attrs:{small:"",color:"error"},on:{click:function(e){t.deleteDialog=!1}}},[t._v("Close")]),i("v-btn",{attrs:{outline:"",small:"",color:"error"},on:{click:t.deleteSubscriber}},[t._v("Delete\n                                            ")])],1)],1)],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("person")])],1),i("v-list-tile-content",[i("v-list-tile-title",[t._v("Username")]),i("p",{staticClass:"mb-0"},[t._v(t._s(t.details.username)+"\n                                    ")])],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("branding_watermark")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Cards prefix",type:"number",rules:[t.rules.rrrCounter,t.rules.number,t.rules.required,t.rules.checkAdminZeros]},model:{value:t.details.rrr,callback:function(e){t.$set(t.details,"rrr",e)},expression:"details.rrr"}})],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("mail")])],1),i("v-list-tile-content",[i("v-list-tile-title",[t._v("Email")]),i("p",{staticClass:"mb-0"},[t._v(t._s(t.details.email))])],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("person")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"First name",type:"text"},model:{value:t.details.first_name,callback:function(e){t.$set(t.details,"first_name",e)},expression:"details.first_name"}})],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Last name",type:"text"},model:{value:t.details.last_name,callback:function(e){t.$set(t.details,"last_name",e)},expression:"details.last_name"}})],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("check")])],1),i("v-list-tile-content",[i("v-list-tile-title",[t._v("Status verification")]),i("p",{staticClass:"mb-0"},[t._v(t._s(t.details.is_activated)+"\n                                    ")])],1)],1),t.$store.getters.isPREPAYMENT?t._e():i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("account_balance_wallet")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Balance",type:"number",rules:[t.rules.counter,t.rules.number,t.rules.required]},model:{value:t.details.balance,callback:function(e){t.$set(t.details,"balance",e)},expression:"details.balance"}})],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Credit",type:"number",rules:[t.rules.counter,t.rules.numberReverse,t.rules.required]},model:{value:t.details.credit,callback:function(e){t.$set(t.details,"credit",e)},expression:"details.credit"}})],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("card_membership")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Card price (materials)",type:"number",rules:[t.rules.counter,t.rules.number,t.rules.required]},model:{value:t.details.price_card,callback:function(e){t.$set(t.details,"price_card",e)},expression:"details.price_card"}})],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("phone")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Phone",type:"number"},model:{value:t.details.telephone,callback:function(e){t.$set(t.details,"telephone",e)},expression:"details.telephone"}})],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("place")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Address",type:"text"},model:{value:t.details.address,callback:function(e){t.$set(t.details,"address",e)},expression:"details.address"}})],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("place")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Zone",type:"text"},model:{value:t.details.zone,callback:function(e){t.$set(t.details,"zone",e)},expression:"details.zone"}})],1)],1),i("v-list-tile",{attrs:{avatar:""},on:{click:function(t){}}},[i("v-list-tile-avatar",[i("v-icon",{staticClass:"grey lighten-1 white--text"},[t._v("comment")])],1),i("v-list-tile-content",[i("v-text-field",{attrs:{label:"Comment",type:"text"},model:{value:t.details.comment,callback:function(e){t.$set(t.details,"comment",e)},expression:"details.comment"}})],1)],1),i("v-list-tile",[i("v-btn",{staticClass:"ml-auto",attrs:{small:"",color:"primary"},on:{click:t.saveResellerInformation}},[t._v("Save\n                                ")])],1)],1)],1)],1)],1)],1)],1)],1)},s=[],r=(i("6b54"),i("bc3a")),n=i.n(r),l={name:"ResellersEdit",data:function(){var t=this;return{snack:!1,snackColor:"",snackText:"",loading:!0,loadingCards:!0,loadingAviableCards:!0,snackbar:!1,dialog:!1,deleteDialog:!1,search:"",text:"Oops... Something went wrong",timeout:5e3,newBalance:"",details:{address:"",balance:0,cards:Array(0),email:""},headers:[{text:"Label",align:"left",value:"label"},{text:"Action",value:"action",sortable:!1}],cards:[],aviableCards:[],rules:{counter:function(t){return t<=2147483647||"Max 2147483647"},rrrCounter:function(t){return t<=999&&t>=0||"Min 0 Max 999"},checkAdminZeros:function(e){return"000"!==e&&"00"!==e&&"0"!==e||t.details.is_superuser||'Only admins can have prefix "000"'},number:function(t){var e=/^\d+$/;return e.test(t)||"Invalid number."},numberReverse:function(t){var e=/^-\d+$/;return e.test(t)||t<=0||"Invalid number."},required:function(t){return!!t||0===t||"Required."},email:function(t){var e=/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;return e.test(t)||"Invalid e-mail."}}}},methods:{getData:function(){var t=this;this.loadingCards=!0,n.a.get("".concat(this.$hostname,"/api/resellers/").concat(this.$route.params.id,"/")).then(function(e){200===e.status&&(t.details=e.data,t.cards=t.details.cards,t.newBalance=t.details.balance,t.loadingCards=!1,t.details.is_activated=t.details.is_activated?"Active":"Inactive",console.log(t.details))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})},deleteSubscriber:function(){var t=this;n.a.delete("".concat(this.$hostname,"/api/resellers/delete/").concat(this.$route.params.id,"/")).then(function(e){204===e.status&&(console.log(e.data),t.$router.push("/resellers"))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0})},saveResellerInformation:function(){var t=this;if(this.$refs.form.validate()){this.loading=!0;var e={username:this.details.username,rrr:this.rrr,first_name:this.details.first_name,last_name:this.details.last_name,address:this.details.address,telephone:this.details.telephone,zone:this.details.zone,balance:this.details.balance,credit:this.details.credit,price_card:this.details.price_card,comment:this.details.comment};n.a.put("".concat(this.$hostname,"/api/resellers/edit/").concat(this.$route.params.id,"/"),e).then(function(e){200===e.status&&(t.getData(),t.text="Settings changed!",t.snackbar=!0,t.dialog=!1,t.loading=!1,setTimeout(function(){t.$router.push("/resellers/".concat(t.$route.params.id,"/details"))},1500))}).catch(function(e){t.text="Connection error",console.log(e),t.snackbar=!0,t.dialog=!1})}else this.text="Fill the form correctly",this.snackbar=!0}},computed:{rrr:function(){return this.details.rrr<10&&this.details.rrr.length<2?"00"+this.details.rrr:this.details.rrr<100&&this.details.rrr.length<3?"0"+this.details.rrr:this.details.rrr.toString()}},beforeCreate:function(){this.$session.exists()||this.$router.push("/"),this.$session.get("isSuperuser")||this.$router.push("/cards")},mounted:function(){this.getData()}},c=l,o=(i("62ba"),i("2877")),d=i("6544"),u=i.n(d),v=i("8336"),h=i("b0af"),m=i("99d9"),p=i("12b2"),f=i("a523"),g=i("549c"),b=i("169a"),_=i("0e8f"),x=i("4bd4"),S=i("132d"),y=i("a722"),C=i("8860"),k=i("ba95"),$=i("c954"),w=i("5d23"),z=i("2db4"),L=i("9910"),V=i("e0c7"),A=i("2677"),R=Object(o["a"])(c,a,s,!1,null,null,null);e["default"]=R.exports;u()(R,{VBtn:v["a"],VCard:h["a"],VCardActions:m["a"],VCardText:m["b"],VCardTitle:p["a"],VContainer:f["a"],VContent:g["a"],VDialog:b["a"],VFlex:_["a"],VForm:x["a"],VIcon:S["a"],VLayout:y["a"],VList:C["a"],VListTile:k["a"],VListTileAvatar:$["a"],VListTileContent:w["a"],VListTileTitle:w["c"],VSnackbar:z["a"],VSpacer:L["a"],VSubheader:V["a"],VTextField:A["a"]})},"4c34":function(t,e,i){},"62ba":function(t,e,i){"use strict";var a=i("0d81"),s=i.n(a);s.a},"99d9":function(t,e,i){"use strict";var a=i("80d2"),s=i("b0af"),r=(i("253d"),i("4c34"),i("23bf")),n=i("58df"),l=Object(n["a"])(r["a"]).extend({name:"v-responsive",props:{aspectRatio:[String,Number]},computed:{computedAspectRatio:function(){return Number(this.aspectRatio)},aspectStyle:function(){return this.computedAspectRatio?{paddingBottom:1/this.computedAspectRatio*100+"%"}:void 0},__cachedSizer:function(){return this.aspectStyle?this.$createElement("div",{style:this.aspectStyle,staticClass:"v-responsive__sizer"}):[]}},methods:{genContent:function(){return this.$createElement("div",{staticClass:"v-responsive__content"},this.$slots.default)}},render:function(t){return t("div",{staticClass:"v-responsive",style:this.measurableStyles,on:this.$listeners},[this.__cachedSizer,this.genContent()])}}),c=l,o=i("d9bd"),d=c.extend({name:"v-img",props:{alt:String,contain:Boolean,src:{type:[String,Object],default:""},gradient:String,lazySrc:String,srcset:String,sizes:String,position:{type:String,default:"center center"},transition:{type:[Boolean,String],default:"fade-transition"}},data:function(){return{currentSrc:"",image:null,isLoading:!0,calculatedAspectRatio:void 0}},computed:{computedAspectRatio:function(){return this.normalisedSrc.aspect},normalisedSrc:function(){return"string"===typeof this.src?{src:this.src,srcset:this.srcset,lazySrc:this.lazySrc,aspect:Number(this.aspectRatio||this.calculatedAspectRatio)}:{src:this.src.src,srcset:this.srcset||this.src.srcset,lazySrc:this.lazySrc||this.src.lazySrc,aspect:Number(this.aspectRatio||this.src.aspect||this.calculatedAspectRatio)}},__cachedImage:function(){if(!this.normalisedSrc.src&&!this.normalisedSrc.lazySrc)return[];var t=[],e=this.isLoading?this.normalisedSrc.lazySrc:this.currentSrc;this.gradient&&t.push("linear-gradient("+this.gradient+")"),e&&t.push('url("'+e+'")');var i=this.$createElement("div",{staticClass:"v-image__image",class:{"v-image__image--preload":this.isLoading,"v-image__image--contain":this.contain,"v-image__image--cover":!this.contain},style:{backgroundImage:t.join(", "),backgroundPosition:this.position},key:+this.isLoading});return this.transition?this.$createElement("transition",{attrs:{name:this.transition,mode:"in-out"}},[i]):i}},watch:{src:function(){this.isLoading?this.loadImage():this.init()},"$vuetify.breakpoint.width":"getSrc"},mounted:function(){this.init()},methods:{init:function(){if(this.normalisedSrc.lazySrc){var t=new Image;t.src=this.normalisedSrc.lazySrc,this.pollForSize(t,null)}this.normalisedSrc.src&&this.loadImage()},onLoad:function(){this.getSrc(),this.isLoading=!1,this.$emit("load",this.src)},onError:function(){Object(o["a"])("Image load failed\n\nsrc: "+this.normalisedSrc.src,this),this.$emit("error",this.src)},getSrc:function(){this.image&&(this.currentSrc=this.image.currentSrc||this.image.src)},loadImage:function(){var t=this,e=new Image;this.image=e,e.onload=function(){e.decode?e.decode().catch(function(e){Object(o["c"])("Failed to decode image, trying to render anyway\n\nsrc: "+t.normalisedSrc.src+(e.message?"\nOriginal error: "+e.message:""),t)}).then(t.onLoad):t.onLoad()},e.onerror=this.onError,e.src=this.normalisedSrc.src,this.sizes&&(e.sizes=this.sizes),this.normalisedSrc.srcset&&(e.srcset=this.normalisedSrc.srcset),this.aspectRatio||this.pollForSize(e),this.getSrc()},pollForSize:function(t){var e=this,i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:100,a=function a(){var s=t.naturalHeight,r=t.naturalWidth;s||r?e.calculatedAspectRatio=r/s:null!=i&&setTimeout(a,i)};a()},__genPlaceholder:function(){if(this.$slots.placeholder){var t=this.isLoading?[this.$createElement("div",{staticClass:"v-image__placeholder"},this.$slots.placeholder)]:[];return this.transition?this.$createElement("transition",{attrs:{name:this.transition}},t):t[0]}}},render:function(t){var e=c.options.render.call(this,t);return e.data.staticClass+=" v-image",e.data.attrs={role:this.alt?"img":void 0,"aria-label":this.alt},e.children=[this.__cachedSizer,this.__cachedImage,this.__genPlaceholder(),this.genContent()],t(e.tag,e.data,e.children)}}),u=d.extend({name:"v-card-media",mounted:function(){Object(o["d"])("v-card-media",this.src?"v-img":"v-responsive",this)}}),v=i("12b2");i.d(e,"a",function(){return h}),i.d(e,"b",function(){return m});var h=Object(a["g"])("v-card__actions"),m=Object(a["g"])("v-card__text");s["a"],v["a"]}}]);
//# sourceMappingURL=chunk-44814fb8.975272b9.js.map