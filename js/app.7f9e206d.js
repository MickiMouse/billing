(function(e){function t(t){for(var r,a,i=t[0],c=t[1],u=t[2],l=0,d=[];l<i.length;l++)a=i[l],s[a]&&d.push(s[a][0]),s[a]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(e[r]=c[r]);h&&h(t);while(d.length)d.shift()();return o.push.apply(o,u||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],r=!0,a=1;a<n.length;a++){var i=n[a];0!==s[i]&&(r=!1)}r&&(o.splice(t--,1),e=c(c.s=n[0]))}return e}var r={},a={app:0},s={app:0},o=[];function i(e){return c.p+"js/"+({}[e]||e)+"."+{"chunk-0202af14":"4271a5f4","chunk-23cfd415":"9021b5ce","chunk-44814fb8":"8ecebafa","chunk-50cf0084":"d5a9a7ca","chunk-0b8497aa":"6e007227","chunk-3f8ef686":"9ede2aa0","chunk-7d3e3cb1":"193d663b","chunk-15b025fd":"01c011e0","chunk-1fd13e29":"45fb637e","chunk-26460a6f":"56557650","chunk-66b05e7d":"b2c13082","chunk-6b69d58f":"dca70f34","chunk-6daab4c6":"27504f6c","chunk-87d5cc82":"851fed0b","chunk-97f3fc86":"5624ef05","chunk-c2b1cb58":"cd8f66cf","chunk-d8e53ad0":"ab67f43e","chunk-e92e044e":"e45056a0"}[e]+".js"}function c(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.e=function(e){var t=[],n={"chunk-0202af14":1,"chunk-23cfd415":1,"chunk-44814fb8":1,"chunk-50cf0084":1,"chunk-0b8497aa":1,"chunk-3f8ef686":1,"chunk-7d3e3cb1":1,"chunk-15b025fd":1,"chunk-1fd13e29":1,"chunk-26460a6f":1,"chunk-66b05e7d":1,"chunk-6b69d58f":1,"chunk-6daab4c6":1,"chunk-87d5cc82":1,"chunk-97f3fc86":1,"chunk-c2b1cb58":1,"chunk-d8e53ad0":1,"chunk-e92e044e":1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=new Promise(function(t,n){for(var r="css/"+({}[e]||e)+"."+{"chunk-0202af14":"aff25974","chunk-23cfd415":"6230adf2","chunk-44814fb8":"aff25974","chunk-50cf0084":"a2f5448e","chunk-0b8497aa":"96bb090d","chunk-3f8ef686":"d2276181","chunk-7d3e3cb1":"1b799464","chunk-15b025fd":"037edcb2","chunk-1fd13e29":"a00e327e","chunk-26460a6f":"a00e327e","chunk-66b05e7d":"037edcb2","chunk-6b69d58f":"e6959ab6","chunk-6daab4c6":"3ed3edb1","chunk-87d5cc82":"037edcb2","chunk-97f3fc86":"037edcb2","chunk-c2b1cb58":"981c42df","chunk-d8e53ad0":"981c42df","chunk-e92e044e":"981c42df"}[e]+".css",s=c.p+r,o=document.getElementsByTagName("link"),i=0;i<o.length;i++){var u=o[i],l=u.getAttribute("data-href")||u.getAttribute("href");if("stylesheet"===u.rel&&(l===r||l===s))return t()}var d=document.getElementsByTagName("style");for(i=0;i<d.length;i++){u=d[i],l=u.getAttribute("data-href");if(l===r||l===s)return t()}var h=document.createElement("link");h.rel="stylesheet",h.type="text/css",h.onload=t,h.onerror=function(t){var r=t&&t.target&&t.target.src||s,o=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");o.code="CSS_CHUNK_LOAD_FAILED",o.request=r,delete a[e],h.parentNode.removeChild(h),n(o)},h.href=s;var f=document.getElementsByTagName("head")[0];f.appendChild(h)}).then(function(){a[e]=0}));var r=s[e];if(0!==r)if(r)t.push(r[2]);else{var o=new Promise(function(t,n){r=s[e]=[t,n]});t.push(r[2]=o);var u,l=document.createElement("script");l.charset="utf-8",l.timeout=120,c.nc&&l.setAttribute("nonce",c.nc),l.src=i(e),u=function(t){l.onerror=l.onload=null,clearTimeout(d);var n=s[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src,o=new Error("Loading chunk "+e+" failed.\n("+r+": "+a+")");o.type=r,o.request=a,n[1](o)}s[e]=void 0}};var d=setTimeout(function(){u({type:"timeout",target:l})},12e4);l.onerror=l.onload=u,document.head.appendChild(l)}return Promise.all(t)},c.m=e,c.c=r,c.d=function(e,t,n){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)c.d(n,r,function(t){return e[t]}.bind(null,r));return n},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="http://157.230.98.28/",c.oe=function(e){throw console.error(e),e};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],l=u.push.bind(u);u.push=t,u=u.slice();for(var d=0;d<u.length;d++)t(u[d]);var h=l;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"56d7":function(e,t,n){"use strict";n.r(t);n("cadf"),n("551c"),n("f751"),n("097d");var r=n("2b0e"),a=n("bb71");n("da64");r["a"].use(a["a"],{iconfont:"md",theme:{primary:"#007bff",secondary:"#f9f9ff",accent:"#2a73ed",error:"#f44336",warning:"#ff5722",info:"#00bcd4",success:"#8bc34a",yellow:"#ffeb3b"}});var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("top-panel"),n("router-view")],1)},o=[],i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return e.show?n("div",[n("v-snackbar",{attrs:{timeout:e.timeout,top:""},model:{value:e.snackbar,callback:function(t){e.snackbar=t},expression:"snackbar"}},[e._v("\n        "+e._s(e.text)+"\n        "),n("v-btn",{attrs:{flat:""},on:{click:function(t){e.snackbar=!1}}},[e._v("\n            Close\n        ")])],1),n("top-panel-menu"),n("v-toolbar",{attrs:{color:"primary",dark:"",extended:"","extension-height":"4",app:""},scopedSlots:e._u([{key:"extension",fn:function(){return[n("v-progress-linear",{directives:[{name:"show",rawName:"v-show",value:e.loading,expression:"loading"}],staticClass:"px-0",attrs:{slot:"extension",indeterminate:!1,color:"secondary",height:"4"},slot:"extension",model:{value:e.loadingPercent,callback:function(t){e.loadingPercent=t},expression:"loadingPercent"}})]},proxy:!0}],null,!1,2642048888)},[n("v-toolbar-side-icon",{on:{click:function(t){return t.stopPropagation(),e.$store.dispatch("switchMenu")}}}),n("v-toolbar-title",{staticClass:"headline text-uppercase"},[n("span",{staticClass:"font-weight-light"},[e._v("Ripple")]),n("span",{staticClass:"font-weight-thin"},[e._v(e._s(this.$route.meta.title))])]),n("v-spacer"),n("v-spacer"),n("v-toolbar-title",{staticClass:"headline text-uppercase"},[n("span",{staticClass:"font-weight-light"},[e._v(e._s(e.formatBalance))])]),e.$session.get("isSuperuser")?n("top-panel-settings"):e._e(),n("v-btn",{attrs:{text:"",flat:"",color:"secondary"},on:{click:e.logout}},[e._v("Logout\n        ")])],1)],1):e._e()},c=[],u=(n("7f7f"),n("bc3a")),l=n.n(u),d=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-navigation-drawer",{attrs:{color:"secondary",app:"",fixed:"",clipped:""},model:{value:e.menuVisible,callback:function(t){e.menuVisible=t},expression:"menuVisible"}},[n("v-divider"),n("v-list",{class:{"pt-3 mt-5":e.$vuetify.breakpoint.mdAndDown,"pt-0 mt-0":e.$vuetify.breakpoint.lgAndUp},attrs:{dense:""}},[n("v-list-tile",[n("v-list-tile-content",[n("v-list-tile-title",[n("span",[e._v("Menu")])])],1)],1),e._l(e.items,function(t){return n("v-list-tile",{key:t.title,attrs:{to:t.route}},[n("v-list-tile-action",[n("v-icon",[e._v(e._s(t.icon))])],1),n("v-list-tile-content",[n("v-list-tile-title",[e._v(e._s(t.title))])],1)],1)})],2)],1)},h=[],f={name:"topPanelMenu",props:{},data:function(){return{items:[{title:"Dashboard",icon:"bar_chart",route:"/dashboard"},{title:"Subscribers",icon:"person",route:"/subscribers"},{title:"Cards",icon:"card_membership",route:"/cards"},{title:"Packages",icon:"archive",route:"/packages"},{title:"Resellers",icon:"people",route:"/resellers"},{title:"Activation",icon:"people",route:"/resellersActivation"},{title:"Reports",icon:"description",route:"/reports"}]}},watch:{},computed:{menuVisible:{get:function(){return this.$store.getters.menuVisible},set:function(e){console.log("set"),this.$store.commit("set",{type:"MenuVisible",items:e})}}},beforeMount:function(){var e=this;this.$session.get("isSuperuser")||(this.items=[{title:"Subscribers",icon:"person",route:"/subscribers"},{title:"Cards",icon:"card_membership",route:"/cards"},{title:"Packages",icon:"archive",route:"/packages"}]),l.a.interceptors.response.use(function(e){return e},function(t){return 401==t.response.status&&(e.$session.destroy(),e.$router.push("/"),l.a.defaults.headers.common["Authorization"]=""),Promise.reject(t)})}},p=f,m=n("2877"),b=n("6544"),v=n.n(b),k=n("ce7e"),g=n("132d"),y=n("8860"),x=n("ba95"),P=n("40fe"),_=n("5d23"),w=n("f774"),C=Object(m["a"])(p,d,h,!1,null,"6a46d4b8",null),S=C.exports;v()(C,{VDivider:k["a"],VIcon:g["a"],VList:y["a"],VListTile:x["a"],VListTileAction:P["a"],VListTileContent:_["a"],VListTileTitle:_["c"],VNavigationDrawer:w["a"]});var A=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-layout",{staticClass:"toppanel-search"},[n("v-autocomplete",{staticClass:"mx-3",attrs:{loading:e.loading,items:e.items,"search-input":e.search,"cache-items":"",flat:"","hide-no-data":"","hide-details":"",label:"Search","solo-inverted":""},on:{"update:searchInput":function(t){e.search=t},"update:search-input":function(t){e.search=t}},model:{value:e.select,callback:function(t){e.select=t},expression:"select"}})],1)},V=[],M={name:"topPanelSearch",data:function(){return{loading:!1,items:[],search:null,select:null,states:["Alabama","Alaska","American Samoa","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Federated States of Micronesia","Florida","Georgia","Guam","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Marshall Islands","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Northern Mariana Islands","Ohio","Oklahoma","Oregon","Palau","Pennsylvania","Puerto Rico","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virgin Island","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]}},watch:{search:function(e){e&&e!==this.select&&this.querySelections(e)}},methods:{querySelections:function(e){var t=this;this.loading=!0,setTimeout(function(){t.items=t.states.filter(function(t){return(t||"").toLowerCase().indexOf((e||"").toLowerCase())>-1}),t.loading=!1},500)}}},$=M,T=n("c6a6"),O=n("a722"),q=Object(m["a"])($,A,V,!1,null,"1c4ef1d7",null),L=q.exports;v()(q,{VAutocomplete:T["a"],VLayout:O["a"]});var E=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{row:"","justify-end":""}},[n("v-dialog",{attrs:{fullscreen:"","hide-overlay":"",transition:"dialog-bottom-transition"},scopedSlots:e._u([{key:"activator",fn:function(t){var r=t.on;return[n("v-btn",e._g({attrs:{color:"white",fab:"",flat:"",dark:""}},r),[n("v-icon",{attrs:{light:""}},[e._v("settings")])],1)]}}]),model:{value:e.dialog,callback:function(t){e.dialog=t},expression:"dialog"}},[n("v-snackbar",{attrs:{timeout:e.timeout,top:""},model:{value:e.snackbar,callback:function(t){e.snackbar=t},expression:"snackbar"}},[e._v("\n            "+e._s(e.text)+"\n            "),n("v-btn",{attrs:{flat:""},on:{click:function(t){e.snackbar=!1}}},[e._v("\n                Close\n            ")])],1),n("v-card",{scopedSlots:e._u([{key:"extension",fn:function(){return[n("v-progress-linear",{directives:[{name:"show",rawName:"v-show",value:e.loading,expression:"loading"}],staticClass:"px-0",attrs:{slot:"extension",indeterminate:!0,color:"secondary",height:"4"},slot:"extension"})]},proxy:!0}])},[n("v-toolbar",{attrs:{dark:"",color:"primary",extended:"","extension-height":"4"}},[n("v-btn",{attrs:{icon:"",dark:""},on:{click:function(t){e.dialog=!1}}},[n("v-icon",[e._v("close")])],1),n("v-toolbar-title",[e._v("Settings")]),n("v-spacer"),n("v-toolbar-items",[n("v-btn",{attrs:{dark:"",flat:""},on:{click:e.saveSettings}},[e._v("Save")])],1)],1),n("v-form",{ref:"form"},[n("v-list",{attrs:{"three-line":"",subheader:""}},[n("v-subheader",[e._v("Payment")]),n("v-list-tile",{attrs:{avatar:""}},[n("v-list-tile-content",[n("v-select",{attrs:{items:e.kind,label:"Choose",solo:"",rules:[e.rules.required]},model:{value:e.kind_payment,callback:function(t){e.kind_payment=t},expression:"kind_payment"}})],1)],1),n("v-list-tile",{attrs:{avatar:""}},[n("v-list-tile-content",[n("v-text-field",{attrs:{label:"Currency",type:"text",rules:[e.rules.currency,e.rules.required]},model:{value:e.currency,callback:function(t){e.currency=t},expression:"currency"}})],1)],1)],1),n("v-divider"),n("v-list",{attrs:{"three-line":"",subheader:""}},[n("v-subheader",[e._v("Payment period")]),n("v-list-tile",{attrs:{avatar:""}},[n("v-list-tile-content",[n("v-select",{attrs:{items:e.period,label:"Choose",solo:"",rules:[e.rules.required]},model:{value:e.kind_period,callback:function(t){e.kind_period=t},expression:"kind_period"}})],1)],1),n("v-list-tile",{attrs:{avatar:""}},[n("v-list-tile-content",[n("v-text-field",{attrs:{label:"Quantity (of payment period)",type:"number",required:"",rules:[e.rules.counter,e.rules.number]},model:{value:e.numberOfPeriod,callback:function(t){e.numberOfPeriod=t},expression:"numberOfPeriod"}})],1)],1)],1),n("v-divider"),n("v-subheader",[e._v("Server preferences:")]),n("v-layout",{attrs:{wrap:"","px-3":""}},[n("v-flex",{attrs:{sm3:"","pr-3":""}},[n("v-text-field",{attrs:{label:"Cards prefix",type:"number",rules:[e.rules.rrrCounter,e.rules.number,e.rules.required]},model:{value:e.sssss,callback:function(t){e.sssss=t},expression:"sssss"}})],1),n("v-flex",{attrs:{sm3:"","pr-3":""}},[n("v-text-field",{attrs:{label:"Max cards",type:"number",rules:[e.rules.cardCounter,e.rules.number,e.rules.required]},model:{value:e.max_cards,callback:function(t){e.max_cards=t},expression:"max_cards"}})],1),n("v-flex",{attrs:{sm3:"","pr-3":""}},[n("v-text-field",{attrs:{label:"Server ip",type:"text",rules:[e.rules.ipAddress,e.rules.required]},model:{value:e.server_ip,callback:function(t){e.server_ip=t},expression:"server_ip"}})],1),n("v-flex",{attrs:{sm3:"","pr-3":""}},[n("v-text-field",{attrs:{label:"Server port",type:"number",rules:[e.rules.portCounter,e.rules.number,e.rules.required]},model:{value:e.server_port,callback:function(t){e.server_port=t},expression:"server_port"}})],1)],1)],1),n("v-divider"),n("v-list",{attrs:{"three-line":"",subheader:""}},[n("v-subheader",[e._v("Bouquets")]),n("v-list-tile",{attrs:{avatar:""}},[n("v-list-tile-content",{staticClass:"no-flex"},[n("v-form",{ref:"formBouquets"},[n("v-text-field",{attrs:{label:"Bouquets",type:"number",rules:[e.rules.bouquetsCounter]},model:{value:e.numOfBouquets,callback:function(t){e.numOfBouquets=t},expression:"numOfBouquets"}})],1)],1),n("v-list-tile-avatar",[n("v-btn",{staticClass:"mr-auto",attrs:{color:"primary",dark:"",small:"",ripple:"",icon:""},on:{click:e.updateBouquets}},[n("v-icon",{attrs:{small:""}},[e._v("autorenew")])],1)],1)],1)],1),n("v-list",{attrs:{"three-line":"",subheader:""}},[n("v-subheader",[e._v("Synchronization")]),n("v-list-tile",{attrs:{avatar:""}},[n("v-list-tile-content",{staticClass:"no-flex"},[n("v-form",{ref:"formBouquets"},[n("v-text-field",{attrs:{label:"Periods quantity",type:"number",rules:[e.rules.counterUpdatePeriods]},model:{value:e.counterUpdatePeriods,callback:function(t){e.counterUpdatePeriods=t},expression:"counterUpdatePeriods"}})],1)],1)],1)],1),n("v-subheader",[e._v("Synchronization at:")]),n("v-layout",{attrs:{wrap:"","px-3":""}},e._l(e.serverPeriods,function(t,r){return n("v-flex",{key:r,attrs:{sm3:"","pr-3":""}},[n("h3",{staticClass:"subheading"},[e._v(e._s(t.value))])])}),1),n("v-subheader",[e._v("New synchronization periods:")]),n("v-form",{ref:"formPeriods",staticClass:"w-100 px-3",on:{submit:function(t){return t.preventDefault(),e.synchronize()}}},[n("v-layout",{attrs:{wrap:""}},e._l(e.counterUpdatePeriodsArray,function(t,r){return n("v-flex",{key:r,attrs:{sm3:"","pr-3":""}},[n("v-menu",{attrs:{id:"menu"+r,"close-on-content-click":!1,"nudge-right":40,"return-value":e.updatePeriodsArray[r].value,transition:"scale-transition","offset-y":"","full-width":"","max-width":"290px","min-width":"290px"},on:{"update:returnValue":function(t){return e.$set(e.updatePeriodsArray[r],"value",t)},"update:return-value":function(t){return e.$set(e.updatePeriodsArray[r],"value",t)}},scopedSlots:e._u([{key:"activator",fn:function(t){var a=t.on;return[n("v-text-field",e._g({attrs:{label:"Period "+(r+1),"prepend-icon":"access_time",readonly:""},model:{value:e.updatePeriodsArrayHack[r].value,callback:function(t){e.$set(e.updatePeriodsArrayHack[r],"value",t)},expression:"updatePeriodsArrayHack[key].value"}},a))]}}],null,!0),model:{value:e.updatePeriodsArray[r].isOpen,callback:function(t){e.$set(e.updatePeriodsArray[r],"isOpen",t)},expression:"updatePeriodsArray[key].isOpen"}},[e.updatePeriodsArray[r].isOpen?n("v-time-picker",{attrs:{format:"24hr","full-width":""},on:{"click:minute":function(t){e.updatePeriodsArrayHack[r].value=e.updatePeriodsArray[r].value}},model:{value:e.updatePeriodsArray[r].value,callback:function(t){e.$set(e.updatePeriodsArray[r],"value",t)},expression:"updatePeriodsArray[key].value"}}):e._e()],1)],1)}),1)],1)],1)],1)],1)},N=[],D=(n("6b54"),n("c5f6"),n("04ff"),{data:function(){return{dialog:!1,snackbar:!1,text:"Oops... Something went wrong",timeout:5e3,loading:!0,kind:[{text:"Virtual balance",value:"VIRTUAL"},{text:"Prepayment",value:"PREPAYMENT"}],currency:"",period:[{text:"Days",value:"DAYS"},{text:"Weeks",value:"WEEKS"},{text:"Months",value:"MONTHS"}],updatePeriodsArray:[{},{},{},{},{},{},{},{}],updatePeriodsArrayHack:[{},{},{},{},{},{},{},{}],counterUpdatePeriods:1,serverPeriods:[],kind_payment:"",kind_period:"",numberOfPeriod:1,max_cards:0,server_ip:"",server_port:"",rules:{required:function(e){return!!e||"Required."},counter:function(e){return e<=100||"Max 100"},currency:function(e){return e.length<=100||"Max 100 characters"},counterUpdatePeriods:function(e){return e<=8&&e>=1||"Min 1 Max 8"},bouquetsCounter:function(e){return e<=128&&e>=1||"Min 1 Max 128"},number:function(e){var t=/^\d+$/;return t.test(e)||"Invalid number."},rrrCounter:function(e){return e<=99999&&e>=0&&e.length<=5||"Min 0 Max 99999"},cardCounter:function(e){return e<=1e5&&e>=0||"Min 0 Max 100000"},ipAddress:function(e){var t=/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;return t.test(e)||"Invalid id address"},portCounter:function(e){return e<=65535&&e>=0||"Min 0 Max 65535"}},sssss:"00000",numOfBouquets:1}},computed:{counterUpdatePeriodsArray:function(){return this.counterUpdatePeriods<1?new Array(1):this.counterUpdatePeriods>8?new Array(8):new Array(Number.parseInt(this.counterUpdatePeriods))},ssssWithZeros:function(){return this.sssss<10&&this.sssss.length<2?"0000"+this.sssss:this.sssss<100&&this.sssss.length<3?"000"+this.sssss:this.sssss<1e3&&this.sssss.length<4?"00"+this.sssss:this.sssss<1e4&&this.sssss.length<5?"0"+this.sssss:this.sssss.toString()}},methods:{getData:function(){var e=this;this.loading=!0,l.a.get("".concat(this.$hostname,"/api/settings/")).then(function(t){200===t.status&&(e.kind_payment=t.data.kind_payment,e.currency=t.data.currency,e.kind_period=t.data.kind_period,e.numberOfPeriod=t.data.quantity,e.sssss=t.data.sssss,e.max_cards=t.data.max_cards,e.server_ip=t.data.server_ip,e.server_port=t.data.server_port,console.log(t.data),e.serverPeriods=t.data.periods,e.loading=!1,e.$store.commit("set",{type:"isPREPAYMENT",items:"PREPAYMENT"===e.kind_payment}),e.$store.commit("set",{type:"currency",items:e.currency}))}).catch(function(t){e.text="Connection error",e.snackbar=!0})},saveSettings:function(){var e=this;this.$refs.form.validate()?(this.loading=!0,l.a.put("".concat(this.$hostname,"/api/change-settings/"),{kind_payment:this.kind_payment,currency:this.currency,kind_period:this.kind_period,quantity:this.numberOfPeriod,sssss:this.ssssWithZeros,max_cards:this.max_cards,server_ip:this.server_ip,server_port:this.server_port}).then(function(t){200===t.status&&(e.getData(),e.text="Settings changed!",e.snackbar=!0,e.dialog=!1,e.loading=!1,e.$router.push("/dashboard"))}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0,e.dialog=!1}),this.synchronize()):(this.text="Fill the form correctly",this.snackbar=!0)},updateBouquets:function(){var e=this;this.$refs.formBouquets.validate()?l.a.get("".concat(this.$hostname,"/api/download/").concat(this.numOfBouquets,"/")).then(function(t){200===t.status&&(e.getData(),e.text="Bouquets updated!",e.snackbar=!0,e.dialog=!1,e.$router.push("/dashboard"))}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0}):(this.text="Fill the number of bouquets correctly",this.snackbar=!0)},synchronize:function(){var e=this;this.$refs.formPeriods.validate()?l.a.post("".concat(this.$hostname,"/api/synchronize/"),{periods:this.updatePeriodsArrayHack}).then(function(t){200===t.status&&(e.getData(),e.text="Periods updated!",e.snackbar=!0,e.dialog=!1,e.$router.push("/dashboard"))}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0}):(this.text="Fill the periods correctly",this.snackbar=!0)}},beforeMount:function(){l.a.defaults.headers.common["Authorization"]="Token "+this.$session.get("jwt"),this.getData()}}),I=D,j=(n("9ec4"),n("8336")),B=n("b0af"),R=n("169a"),U=n("0e8f"),z=n("4bd4"),H=n("c954"),F=n("e449"),W=n("8e36"),Y=n("b56d"),K=n("2db4"),J=n("9910"),G=n("e0c7"),Z=n("2677"),Q=n("c964"),X=n("71d9"),ee=n("2a7f"),te=Object(m["a"])(I,E,N,!1,null,"537439ac",null),ne=te.exports;v()(te,{VBtn:j["a"],VCard:B["a"],VDialog:R["a"],VDivider:k["a"],VFlex:U["a"],VForm:z["a"],VIcon:g["a"],VLayout:O["a"],VList:y["a"],VListTile:x["a"],VListTileAvatar:H["a"],VListTileContent:_["a"],VMenu:F["a"],VProgressLinear:W["a"],VSelect:Y["a"],VSnackbar:K["a"],VSpacer:J["a"],VSubheader:G["a"],VTextField:Z["a"],VTimePicker:Q["a"],VToolbar:X["a"],VToolbarItems:ee["a"],VToolbarTitle:ee["b"]});var re={name:"topPanel",components:{TopPanelSettings:ne,TopPanelSearch:L,TopPanelMenu:S},data:function(){return{drawer:!1,loadingPercent:0,loadTime:0,interval:null,loading:!0,snackbar:!1,text:"Oops... Something went wrong",timeout:5e3,balance:0}},created:function(){var e=window.performance.timing,t=Math.abs(e.loadEventEnd-e.navigationStart);this.loadTime=100*parseInt(t/1e3%60),this.doProgress()},watch:{loadingPercent:function(e){e>=100&&(this.loading=!1,clearInterval(this.interval))}},methods:{doProgress:function(){var e=this,t=this.loadTime/100;this.interval=setInterval(function(){e.loadingPercent++},t)},logout:function(){var e=this;l.a.post("".concat(this.$hostname,"/api/token/logout/")).then(function(t){console.log(t.data),200===t.status&&(e.text="Successful",e.snackbar=!0,e.$session.destroy(),e.$router.push("/"),l.a.defaults.headers.common["Authorization"]="")}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0,e.$session.destroy(),e.$router.push("/"),l.a.defaults.headers.common["Authorization"]=""})}},computed:{show:function(){return"login"!==this.$route.name&&"login token"!==this.$route.name&&"register"!==this.$route.name&&"forgot"!==this.$route.name},formatBalance:function(){return String(this.balance+this.$store.getters.currency)}},mounted:function(){var e=this;this.$session.get("jwt")&&(l.a.defaults.headers.common["Authorization"]="Token "+this.$session.get("jwt"),l.a.get("".concat(this.$hostname,"/api/balance/")).then(function(t){console.log(t),200===t.status&&(e.balance=t.data.balance)}).catch(function(t){e.text="Connection error",console.log(t),e.snackbar=!0}))}},ae=re,se=(n("89f3"),n("706c")),oe=Object(m["a"])(ae,i,c,!1,null,null,null),ie=oe.exports;v()(oe,{VBtn:j["a"],VProgressLinear:W["a"],VSnackbar:K["a"],VSpacer:J["a"],VToolbar:X["a"],VToolbarSideIcon:se["a"],VToolbarTitle:ee["b"]});var ce={name:"App",components:{TopPanel:ie},data:function(){return{}},computed:{},methods:{},mounted:function(){}},ue=ce,le=(n("5c0b"),n("7496")),de=Object(m["a"])(ue,s,o,!1,null,null,null),he=de.exports;v()(de,{VApp:le["a"]});var fe=n("8c4f");r["a"].use(fe["a"]);var pe=new fe["a"]({mode:"history",routes:[{path:"/",redirect:{name:"login"}},{path:"/register",name:"register",component:function(){return n.e("chunk-c2b1cb58").then(n.bind(null,"7c9c"))},meta:{title:"Register"}},{path:"/login/:token",name:"login token",component:function(){return n.e("chunk-e92e044e").then(n.bind(null,"7101"))},meta:{title:"Login"}},{path:"/login",name:"login",component:function(){return n.e("chunk-e92e044e").then(n.bind(null,"7101"))},meta:{title:"Login"}},{path:"/forgot",name:"forgot",component:function(){return n.e("chunk-d8e53ad0").then(n.bind(null,"37c9"))},meta:{title:"Login"}},{path:"/password/:token",name:"forgot",component:function(){return n.e("chunk-d8e53ad0").then(n.bind(null,"37c9"))},meta:{title:"Login"}},{path:"/dashboard",name:"dashboard",component:function(){return n.e("chunk-23cfd415").then(n.bind(null,"1c62"))},meta:{title:"Dashboard"}},{path:"/subscribers",name:"subscribers",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-97f3fc86")]).then(n.bind(null,"3ac2"))},meta:{title:"Subscribers"}},{path:"/subscribers/:id/details",name:"subscribers details",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-15b025fd")]).then(n.bind(null,"d84c"))},meta:{title:"Subscribers"}},{path:"/subscribers/:id/edit",name:"subscribers edit",component:function(){return n.e("chunk-0202af14").then(n.bind(null,"91f5"))},meta:{title:"Subscribers"}},{path:"/cards",name:"cards",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-0b8497aa"),n.e("chunk-3f8ef686")]).then(n.bind(null,"4b26"))},meta:{title:"Cards"}},{path:"/cards/:id/details",name:"cards details",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-6b69d58f")]).then(n.bind(null,"b06d"))},meta:{title:"Cards"}},{path:"/packages",name:"packages",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-87d5cc82")]).then(n.bind(null,"3f19"))},meta:{title:"Packages"}},{path:"/packages/:id/details",name:"packages details",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-66b05e7d")]).then(n.bind(null,"00da"))},meta:{title:"Packages"}},{path:"/resellers",name:"resellers",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-26460a6f")]).then(n.bind(null,"143e"))},meta:{title:"Resellers"}},{path:"/resellersActivation",name:"resellers activation",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-1fd13e29")]).then(n.bind(null,"6fba"))},meta:{title:"Resellers"}},{path:"/resellers/:id/details",name:"resellers details",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-0b8497aa"),n.e("chunk-7d3e3cb1")]).then(n.bind(null,"59a4"))},meta:{title:"Resellers"}},{path:"/resellers/:id/edit",name:"resellers edit",component:function(){return n.e("chunk-44814fb8").then(n.bind(null,"3828"))},meta:{title:"Resellers"}},{path:"/reports",name:"reports",component:function(){return Promise.all([n.e("chunk-50cf0084"),n.e("chunk-6daab4c6")]).then(n.bind(null,"fb8a"))},meta:{title:"Reports"}}]});pe.beforeEach(function(e,t,n){document.title=e.meta.title+" | Ripple",n()});var me=pe,be=n("2f62"),ve={state:{isSuperuser:!1},mutations:{},getters:{isSuperuser:function(e){return e.isSuperuser}}},ke={state:{lessonsCount:31},mutations:{},getters:{LessonsCount:function(e){return e.lessonsCount}}},ge={state:{},mutations:{},getters:{globalProgress:function(e,t){return console.log(t.LessonsCount,t.PassedLessonsCounter),Math.floor(t.PassedLessonsCounter/t.LessonsCount*100)}}};r["a"].use(be["a"]);var ye=new be["a"].Store({modules:[ve,ke,ge],state:{MenuVisible:!1,isPREPAYMENT:!1,currency:"$"},getters:{menuVisible:function(e){return e.MenuVisible},isPREPAYMENT:function(e){return e.isPREPAYMENT},currency:function(e){return e.currency}},mutations:{set:function(e,t){var n=t.type,r=t.items;e[n]=r}},actions:{switchMenu:function(e){var t=e.commit,n=!this.getters.menuVisible;t("set",{type:"MenuVisible",items:n})}}}),xe=(n("c789"),n("1321")),Pe=n.n(xe),_e=n("0628"),we=n.n(_e);r["a"].use(we.a),r["a"].config.productionTip=!1,r["a"].use(Pe.a),r["a"].component("apexchart",Pe.a),r["a"].prototype.$hostname="http://157.230.98.28",new r["a"]({router:me,store:ye,render:function(e){return e(he)}}).$mount("#app")},"5c0b":function(e,t,n){"use strict";var r=n("6879"),a=n.n(r);a.a},6879:function(e,t,n){},"89f3":function(e,t,n){"use strict";var r=n("ab4b"),a=n.n(r);a.a},9789:function(e,t,n){},"9ec4":function(e,t,n){"use strict";var r=n("9789"),a=n.n(r);a.a},ab4b:function(e,t,n){}});
//# sourceMappingURL=app.7f9e206d.js.map