import{W as ve,r as g,y as H,w as _,d as i,a6 as pe,g as V,i as me,o as K,ae as ge,a0 as be,a4 as he,v as ye,x as Ce,U as qe,a2 as _e,h as a,q as E,T as xe,j as Se,c as ne}from"./index.01f3f215.js";import{Q as X,i as we}from"./QBtn.e62c2945.js";import{a as ue,u as ae}from"./use-dark.9ed0a3a8.js";import{h as A}from"./render.5369a479.js";let j,z=0;const f=new Array(256);for(let e=0;e<256;e++)f[e]=(e+256).toString(16).substring(1);const Be=(()=>{const e=typeof crypto!="undefined"?crypto:typeof window!="undefined"?window.crypto||window.msCrypto:void 0;if(e!==void 0){if(e.randomBytes!==void 0)return e.randomBytes;if(e.getRandomValues!==void 0)return o=>{const t=new Uint8Array(o);return e.getRandomValues(t),t}}return o=>{const t=[];for(let r=o;r>0;r--)t.push(Math.floor(Math.random()*256));return t}})(),Y=4096;function L(){(j===void 0||z+16>Y)&&(z=0,j=Be(Y));const e=Array.prototype.slice.call(j,z,z+=16);return e[6]=e[6]&15|64,e[8]=e[8]&63|128,f[e[0]]+f[e[1]]+f[e[2]]+f[e[3]]+"-"+f[e[4]]+f[e[5]]+"-"+f[e[6]]+f[e[7]]+"-"+f[e[8]]+f[e[9]]+"-"+f[e[10]]+f[e[11]]+f[e[12]]+f[e[13]]+f[e[14]]+f[e[15]]}function Fe(e){return e==null?null:e}function ee(e,o){return e==null?o===!0?`f_${L()}`:null:e}function Re({getValue:e,required:o=!0}={}){if(ve.value===!0){const t=e!==void 0?g(Fe(e())):g(null);return o===!0&&t.value===null&&H(()=>{t.value=`f_${L()}`}),e!==void 0&&_(e,r=>{t.value=ee(r,o)}),t}return e!==void 0?i(()=>ee(e(),o)):g(`f_${L()}`)}const oe=/^on[A-Z]/;function Ae(){const{attrs:e,vnode:o}=V(),t={listeners:g({}),attributes:g({})};function r(){const d={},s={};for(const u in e)u!=="class"&&u!=="style"&&oe.test(u)===!1&&(d[u]=e[u]);for(const u in o.props)oe.test(u)===!0&&(s[u]=o.props[u]);t.attributes.value=d,t.listeners.value=s}return pe(r),r(),t}function Ve({validate:e,resetValidation:o,requiresQForm:t}){const r=me(ge,!1);if(r!==!1){const{props:d,proxy:s}=V();Object.assign(s,{validate:e,resetValidation:o}),_(()=>d.disable,u=>{u===!0?(typeof o=="function"&&o(),r.unbindComponent(s)):r.bindComponent(s)}),H(()=>{d.disable!==!0&&r.bindComponent(s)}),K(()=>{d.disable!==!0&&r.unbindComponent(s)})}else t===!0&&console.error("Parent QForm not found on useFormChild()!")}const te=/^#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$/,le=/^#[0-9a-fA-F]{4}([0-9a-fA-F]{4})?$/,re=/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/,M=/^rgb\(((0|[1-9][\d]?|1[\d]{0,2}|2[\d]?|2[0-4][\d]|25[0-5]),){2}(0|[1-9][\d]?|1[\d]{0,2}|2[\d]?|2[0-4][\d]|25[0-5])\)$/,O=/^rgba\(((0|[1-9][\d]?|1[\d]{0,2}|2[\d]?|2[0-4][\d]|25[0-5]),){2}(0|[1-9][\d]?|1[\d]{0,2}|2[\d]?|2[0-4][\d]|25[0-5]),(0|0\.[0-9]+[1-9]|0\.[1-9]+|1)\)$/,Q={date:e=>/^-?[\d]+\/[0-1]\d\/[0-3]\d$/.test(e),time:e=>/^([0-1]?\d|2[0-3]):[0-5]\d$/.test(e),fulltime:e=>/^([0-1]?\d|2[0-3]):[0-5]\d:[0-5]\d$/.test(e),timeOrFulltime:e=>/^([0-1]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?$/.test(e),email:e=>/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(e),hexColor:e=>te.test(e),hexaColor:e=>le.test(e),hexOrHexaColor:e=>re.test(e),rgbColor:e=>M.test(e),rgbaColor:e=>O.test(e),rgbOrRgbaColor:e=>M.test(e)||O.test(e),hexOrRgbColor:e=>te.test(e)||M.test(e),hexaOrRgbaColor:e=>le.test(e)||O.test(e),anyColor:e=>re.test(e)||M.test(e)||O.test(e)},ke=[!0,!1,"ondemand"],$e={modelValue:{},error:{type:Boolean,default:null},errorMessage:String,noErrorIcon:Boolean,rules:Array,reactiveRules:Boolean,lazyRules:{type:[Boolean,String],default:!1,validator:e=>ke.includes(e)}};function Ee(e,o){const{props:t,proxy:r}=V(),d=g(!1),s=g(null),u=g(!1);Ve({validate:B,resetValidation:w});let v=0,b;const k=i(()=>t.rules!==void 0&&t.rules!==null&&t.rules.length!==0),h=i(()=>t.disable!==!0&&k.value===!0&&o.value===!1),S=i(()=>t.error===!0||d.value===!0),D=i(()=>typeof t.errorMessage=="string"&&t.errorMessage.length!==0?t.errorMessage:s.value);_(()=>t.modelValue,()=>{u.value=!0,h.value===!0&&t.lazyRules===!1&&C()});function $(){t.lazyRules!=="ondemand"&&h.value===!0&&u.value===!0&&C()}_(()=>t.reactiveRules,y=>{y===!0?b===void 0&&(b=_(()=>t.rules,$,{immediate:!0,deep:!0})):b!==void 0&&(b(),b=void 0)},{immediate:!0}),_(()=>t.lazyRules,$),_(e,y=>{y===!0?u.value=!0:h.value===!0&&t.lazyRules!=="ondemand"&&C()});function w(){v++,o.value=!1,u.value=!1,d.value=!1,s.value=null,C.cancel()}function B(y=t.modelValue){if(t.disable===!0||k.value===!1)return!0;const F=++v,T=o.value!==!0?()=>{u.value=!0}:()=>{},q=(c,p)=>{c===!0&&T(),d.value=c,s.value=p||null,o.value=!1},R=[];for(let c=0;c<t.rules.length;c++){const p=t.rules[c];let m;if(typeof p=="function"?m=p(y,Q):typeof p=="string"&&Q[p]!==void 0&&(m=Q[p](y)),m===!1||typeof m=="string")return q(!0,m),!1;m!==!0&&m!==void 0&&R.push(m)}return R.length===0?(q(!1),!0):(o.value=!0,Promise.all(R).then(c=>{if(c===void 0||Array.isArray(c)===!1||c.length===0)return F===v&&q(!1),!0;const p=c.find(m=>m===!1||typeof m=="string");return F===v&&q(p!==void 0,p),p===void 0},c=>(F===v&&(console.error(c),q(!0)),!1)))}const C=be(B,0);return K(()=>{b!==void 0&&b(),C.cancel()}),Object.assign(r,{resetValidation:w,validate:B}),he(r,"hasError",()=>S.value),{isDirtyModel:u,hasRules:k,hasError:S,errorMessage:D,validate:B,resetValidation:w}}let x=[],I=[];function ie(e){I=I.filter(o=>o!==e)}function Ke(e){ie(e),I.push(e)}function Ne(e){ie(e),I.length===0&&x.length!==0&&(x[x.length-1](),x=[])}function Ie(e){I.length===0?e():x.push(e)}function Pe(e){x=x.filter(o=>o!==e)}function ze(e){return e!=null&&(""+e).length!==0}const Me={...ae,...$e,label:String,stackLabel:Boolean,hint:String,hideHint:Boolean,prefix:String,suffix:String,labelColor:String,color:String,bgColor:String,filled:Boolean,outlined:Boolean,borderless:Boolean,standout:[Boolean,String],square:Boolean,loading:Boolean,labelSlot:Boolean,bottomSlots:Boolean,hideBottomSpace:Boolean,rounded:Boolean,dense:Boolean,itemAligned:Boolean,counter:Boolean,clearable:Boolean,clearIcon:String,disable:Boolean,readonly:Boolean,autofocus:Boolean,for:String},Ze={...Me,maxlength:[Number,String]},We=["update:modelValue","clear","focus","blur"];function Je({requiredForAttr:e=!0,tagProp:o,changeEvent:t=!1}={}){const{props:r,proxy:d}=V(),s=ue(r,d.$q),u=Re({required:e,getValue:()=>r.for});return{requiredForAttr:e,changeEvent:t,tag:o===!0?i(()=>r.tag):{value:"label"},isDark:s,editable:i(()=>r.disable!==!0&&r.readonly!==!0),innerLoading:g(!1),focused:g(!1),hasPopupOpen:!1,splitAttrs:Ae(),targetUid:u,rootRef:g(null),targetRef:g(null),controlRef:g(null)}}function Ge(e){const{props:o,emit:t,slots:r,attrs:d,proxy:s}=V(),{$q:u}=s;let v=null;e.hasValue===void 0&&(e.hasValue=i(()=>ze(o.modelValue))),e.emitValue===void 0&&(e.emitValue=l=>{t("update:modelValue",l)}),e.controlEvents===void 0&&(e.controlEvents={onFocusin:N,onFocusout:Z}),Object.assign(e,{clearValue:U,onControlFocusin:N,onControlFocusout:Z,focus:p}),e.computedCounter===void 0&&(e.computedCounter=i(()=>{if(o.counter!==!1){const l=typeof o.modelValue=="string"||typeof o.modelValue=="number"?(""+o.modelValue).length:Array.isArray(o.modelValue)===!0?o.modelValue.length:0,n=o.maxlength!==void 0?o.maxlength:o.maxValues;return l+(n!==void 0?" / "+n:"")}}));const{isDirtyModel:b,hasRules:k,hasError:h,errorMessage:S,resetValidation:D}=Ee(e.focused,e.innerLoading),$=e.floatingLabel!==void 0?i(()=>o.stackLabel===!0||e.focused.value===!0||e.floatingLabel.value===!0):i(()=>o.stackLabel===!0||e.focused.value===!0||e.hasValue.value===!0),w=i(()=>o.bottomSlots===!0||o.hint!==void 0||k.value===!0||o.counter===!0||o.error!==null),B=i(()=>o.filled===!0?"filled":o.outlined===!0?"outlined":o.borderless===!0?"borderless":o.standout?"standout":"standard"),C=i(()=>`q-field row no-wrap items-start q-field--${B.value}`+(e.fieldClass!==void 0?` ${e.fieldClass.value}`:"")+(o.rounded===!0?" q-field--rounded":"")+(o.square===!0?" q-field--square":"")+($.value===!0?" q-field--float":"")+(F.value===!0?" q-field--labeled":"")+(o.dense===!0?" q-field--dense":"")+(o.itemAligned===!0?" q-field--item-aligned q-item-type":"")+(e.isDark.value===!0?" q-field--dark":"")+(e.getControl===void 0?" q-field--auto-height":"")+(e.focused.value===!0?" q-field--focused":"")+(h.value===!0?" q-field--error":"")+(h.value===!0||e.focused.value===!0?" q-field--highlighted":"")+(o.hideBottomSpace!==!0&&w.value===!0?" q-field--with-bottom":"")+(o.disable===!0?" q-field--disabled":o.readonly===!0?" q-field--readonly":"")),y=i(()=>"q-field__control relative-position row no-wrap"+(o.bgColor!==void 0?` bg-${o.bgColor}`:"")+(h.value===!0?" text-negative":typeof o.standout=="string"&&o.standout.length!==0&&e.focused.value===!0?` ${o.standout}`:o.color!==void 0?` text-${o.color}`:"")),F=i(()=>o.labelSlot===!0||o.label!==void 0),T=i(()=>"q-field__label no-pointer-events absolute ellipsis"+(o.labelColor!==void 0&&h.value!==!0?` text-${o.labelColor}`:"")),q=i(()=>({id:e.targetUid.value,editable:e.editable.value,focused:e.focused.value,floatingLabel:$.value,modelValue:o.modelValue,emitValue:e.emitValue})),R=i(()=>{const l={};return e.targetUid.value&&(l.for=e.targetUid.value),o.disable===!0&&(l["aria-disabled"]="true"),l});function c(){const l=document.activeElement;let n=e.targetRef!==void 0&&e.targetRef.value;n&&(l===null||l.id!==e.targetUid.value)&&(n.hasAttribute("tabindex")===!0||(n=n.querySelector("[tabindex]")),n&&n!==l&&n.focus({preventScroll:!0}))}function p(){Ie(c)}function m(){Pe(c);const l=document.activeElement;l!==null&&e.rootRef.value.contains(l)&&l.blur()}function N(l){v!==null&&(clearTimeout(v),v=null),e.editable.value===!0&&e.focused.value===!1&&(e.focused.value=!0,t("focus",l))}function Z(l,n){v!==null&&clearTimeout(v),v=setTimeout(()=>{v=null,!(document.hasFocus()===!0&&(e.hasPopupOpen===!0||e.controlRef===void 0||e.controlRef.value===null||e.controlRef.value.contains(document.activeElement)!==!1))&&(e.focused.value===!0&&(e.focused.value=!1,t("blur",l)),n!==void 0&&n())})}function U(l){ye(l),u.platform.is.mobile!==!0?(e.targetRef!==void 0&&e.targetRef.value||e.rootRef.value).focus():e.rootRef.value.contains(document.activeElement)===!0&&document.activeElement.blur(),o.type==="file"&&(e.inputRef.value.value=null),t("update:modelValue",null),e.changeEvent===!0&&t("change",null),t("clear",o.modelValue),Ce(()=>{const n=b.value;D(),b.value=n})}function se(l){[13,32].includes(l.keyCode)&&U(l)}function de(){const l=[];return r.prepend!==void 0&&l.push(a("div",{class:"q-field__prepend q-field__marginal row no-wrap items-center",key:"prepend",onClick:E},r.prepend())),l.push(a("div",{class:"q-field__control-container col relative-position row no-wrap q-anchor--skip"},fe())),h.value===!0&&o.noErrorIcon===!1&&l.push(P("error",[a(X,{name:u.iconSet.field.error,color:"negative"})])),o.loading===!0||e.innerLoading.value===!0?l.push(P("inner-loading-append",r.loading!==void 0?r.loading():[a(we,{color:o.color})])):o.clearable===!0&&e.hasValue.value===!0&&e.editable.value===!0&&l.push(P("inner-clearable-append",[a(X,{class:"q-field__focusable-action",name:o.clearIcon||u.iconSet.field.clear,tabindex:0,role:"button","aria-label":u.lang.label.clear,onKeyup:se,onClick:U})])),r.append!==void 0&&l.push(a("div",{class:"q-field__append q-field__marginal row no-wrap items-center",key:"append",onClick:E},r.append())),e.getInnerAppend!==void 0&&l.push(P("inner-append",e.getInnerAppend())),e.getControlChild!==void 0&&l.push(e.getControlChild()),l}function fe(){const l=[];return o.prefix!==void 0&&o.prefix!==null&&l.push(a("div",{class:"q-field__prefix no-pointer-events row items-center"},o.prefix)),e.getShadowControl!==void 0&&e.hasShadow.value===!0&&l.push(e.getShadowControl()),e.getControl!==void 0?l.push(e.getControl()):r.rawControl!==void 0?l.push(r.rawControl()):r.control!==void 0&&l.push(a("div",{ref:e.targetRef,class:"q-field__native row",tabindex:-1,...e.splitAttrs.attributes.value,"data-autofocus":o.autofocus===!0||void 0},r.control(q.value))),F.value===!0&&l.push(a("div",{class:T.value},A(r.label,o.label))),o.suffix!==void 0&&o.suffix!==null&&l.push(a("div",{class:"q-field__suffix no-pointer-events row items-center"},o.suffix)),l.concat(A(r.default))}function ce(){let l,n;h.value===!0?S.value!==null?(l=[a("div",{role:"alert"},S.value)],n=`q--slot-error-${S.value}`):(l=A(r.error),n="q--slot-error"):(o.hideHint!==!0||e.focused.value===!0)&&(o.hint!==void 0?(l=[a("div",o.hint)],n=`q--slot-hint-${o.hint}`):(l=A(r.hint),n="q--slot-hint"));const J=o.counter===!0||r.counter!==void 0;if(o.hideBottomSpace===!0&&J===!1&&l===void 0)return;const G=a("div",{key:n,class:"q-field__messages col"},l);return a("div",{class:"q-field__bottom row items-start q-field__bottom--"+(o.hideBottomSpace!==!0?"animated":"stale"),onClick:E},[o.hideBottomSpace===!0?G:a(xe,{name:"q-transition--field-message"},()=>G),J===!0?a("div",{class:"q-field__counter"},r.counter!==void 0?r.counter():e.computedCounter.value):null])}function P(l,n){return n===null?null:a("div",{key:l,class:"q-field__append q-field__marginal row no-wrap items-center q-anchor--skip"},n)}let W=!1;return qe(()=>{W=!0}),_e(()=>{W===!0&&o.autofocus===!0&&s.focus()}),o.autofocus===!0&&H(()=>{s.focus()}),K(()=>{v!==null&&clearTimeout(v)}),Object.assign(s,{focus:p,blur:m}),function(){const n=e.getControl===void 0&&r.control===void 0?{...e.splitAttrs.attributes.value,"data-autofocus":o.autofocus===!0||void 0,...R.value}:R.value;return a(e.tag.value,{ref:e.rootRef,class:[C.value,d.class],style:d.style,...n},[r.before!==void 0?a("div",{class:"q-field__before q-field__marginal row no-wrap items-center",onClick:E},r.before()):null,a("div",{class:"q-field__inner relative-position col self-stretch"},[a("div",{ref:e.controlRef,class:y.value,tabindex:-1,...e.controlEvents},de()),w.value===!0?ce():null]),r.after!==void 0?a("div",{class:"q-field__after q-field__marginal row no-wrap items-center",onClick:E},r.after()):null])}}const Xe={name:String};function Ye(e={}){return(o,t,r)=>{o[t](a("input",{class:"hidden"+(r||""),...e.value}))}}function eo(e){return i(()=>e.name||e.for)}const Oe=/[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]/,De=/[\u4e00-\u9fff\u3400-\u4dbf\u{20000}-\u{2a6df}\u{2a700}-\u{2b73f}\u{2b740}-\u{2b81f}\u{2b820}-\u{2ceaf}\uf900-\ufaff\u3300-\u33ff\ufe30-\ufe4f\uf900-\ufaff\u{2f800}-\u{2fa1f}]/u,Te=/[\u3131-\u314e\u314f-\u3163\uac00-\ud7a3]/,Ue=/[a-z0-9_ -]$/i;function oo(e){return function(t){if(t.type==="compositionend"||t.type==="change"){if(t.target.qComposing!==!0)return;t.target.qComposing=!1,e(t)}else t.type==="compositionupdate"&&t.target.qComposing!==!0&&typeof t.data=="string"&&(Se.is.firefox===!0?Ue.test(t.data)===!1:Oe.test(t.data)===!0||De.test(t.data)===!0||Te.test(t.data)===!0)===!0&&(t.target.qComposing=!0)}}var to=ne({name:"QCardSection",props:{tag:{type:String,default:"div"},horizontal:Boolean},setup(e,{slots:o}){const t=i(()=>`q-card__section q-card__section--${e.horizontal===!0?"horiz row no-wrap":"vert"}`);return()=>a(e.tag,{class:t.value},A(o.default))}}),lo=ne({name:"QCard",props:{...ae,tag:{type:String,default:"div"},square:Boolean,flat:Boolean,bordered:Boolean},setup(e,{slots:o}){const{proxy:{$q:t}}=V(),r=ue(e,t),d=i(()=>"q-card"+(r.value===!0?" q-card--dark q-dark":"")+(e.bordered===!0?" q-card--bordered":"")+(e.square===!0?" q-card--square no-border-radius":"")+(e.flat===!0?" q-card--flat no-shadow":""));return()=>a(e.tag,{class:d.value},A(o.default))}});export{lo as Q,to as a,We as b,Ge as c,Je as d,Ke as e,Ie as f,Xe as g,eo as h,ze as i,oo as j,Ye as k,Ne as r,Ze as u};