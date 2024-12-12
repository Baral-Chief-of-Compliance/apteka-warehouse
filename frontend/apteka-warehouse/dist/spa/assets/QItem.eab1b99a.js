import{c as x,d,h as k,g as B,o as D,R,w as A,y as Y,x as I,j as w,Q as m,v as K,S as N,U as O,V as G,r as Q,P as J}from"./index.01f3f215.js";import{h as H,a as Z}from"./render.5369a479.js";import{u as F,a as X}from"./use-dark.9ed0a3a8.js";import{v as ee,b as te,u as le,c as oe}from"./QBtn.e62c2945.js";import{g as ie,a as ne,h as ae}from"./scroll.7e6533da.js";var be=x({name:"QItemLabel",props:{overline:Boolean,caption:Boolean,header:Boolean,lines:[Number,String]},setup(e,{slots:t}){const l=d(()=>parseInt(e.lines,10)),o=d(()=>"q-item__label"+(e.overline===!0?" q-item__label--overline text-overline":"")+(e.caption===!0?" q-item__label--caption text-caption":"")+(e.header===!0?" q-item__label--header":"")+(l.value===1?" ellipsis":"")),i=d(()=>e.lines!==void 0&&l.value>1?{overflow:"hidden",display:"-webkit-box","-webkit-box-orient":"vertical","-webkit-line-clamp":l.value}:null);return()=>k("div",{style:i.value,class:o.value},H(t.default))}}),pe=x({name:"QList",props:{...F,bordered:Boolean,dense:Boolean,separator:Boolean,padding:Boolean,tag:{type:String,default:"div"}},setup(e,{slots:t}){const l=B(),o=X(e,l.proxy.$q),i=d(()=>"q-list"+(e.bordered===!0?" q-list--bordered":"")+(e.dense===!0?" q-list--dense":"")+(e.separator===!0?" q-list--separator":"")+(o.value===!0?" q-list--dark":"")+(e.padding===!0?" q-list--padding":""));return()=>k(e.tag,{class:i.value},H(t.default))}});function we(e,t,l){let o;function i(){o!==void 0&&(R.remove(o),o=void 0)}return D(()=>{e.value===!0&&i()}),{removeFromHistory:i,addToHistory(){o={condition:()=>l.value===!0,handler:t},R.add(o)}}}const ye={modelValue:{type:Boolean,default:null},"onUpdate:modelValue":[Function,Array]},he=["beforeShow","show","beforeHide","hide"];function ge({showing:e,canShow:t,hideOnRouteChange:l,handleShow:o,handleHide:i,processOnMount:f}){const r=B(),{props:s,emit:c,proxy:L}=r;let u;function p(n){e.value===!0?h(n):y(n)}function y(n){if(s.disable===!0||n!==void 0&&n.qAnchorHandled===!0||t!==void 0&&t(n)!==!0)return;const a=s["onUpdate:modelValue"]!==void 0;a===!0&&(c("update:modelValue",!0),u=n,I(()=>{u===n&&(u=void 0)})),(s.modelValue===null||a===!1)&&v(n)}function v(n){e.value!==!0&&(e.value=!0,c("beforeShow",n),o!==void 0?o(n):c("show",n))}function h(n){if(s.disable===!0)return;const a=s["onUpdate:modelValue"]!==void 0;a===!0&&(c("update:modelValue",!1),u=n,I(()=>{u===n&&(u=void 0)})),(s.modelValue===null||a===!1)&&T(n)}function T(n){e.value!==!1&&(e.value=!1,c("beforeHide",n),i!==void 0?i(n):c("hide",n))}function S(n){s.disable===!0&&n===!0?s["onUpdate:modelValue"]!==void 0&&c("update:modelValue",!1):n===!0!==e.value&&(n===!0?v:T)(u)}A(()=>s.modelValue,S),l!==void 0&&ee(r)===!0&&A(()=>L.$route.fullPath,()=>{l.value===!0&&e.value===!0&&h()}),f===!0&&Y(()=>{S(s.modelValue)});const E={show:y,hide:h,toggle:p};return Object.assign(L,E),E}let g=0,V,P,q,C=!1,$,U,W,b=null;function re(e){se(e)&&K(e)}function se(e){if(e.target===document.body||e.target.classList.contains("q-layout__backdrop"))return!0;const t=N(e),l=e.shiftKey&&!e.deltaX,o=!l&&Math.abs(e.deltaX)<=Math.abs(e.deltaY),i=l||o?e.deltaY:e.deltaX;for(let f=0;f<t.length;f++){const r=t[f];if(ae(r,o))return o?i<0&&r.scrollTop===0?!0:i>0&&r.scrollTop+r.clientHeight===r.scrollHeight:i<0&&r.scrollLeft===0?!0:i>0&&r.scrollLeft+r.clientWidth===r.scrollWidth}return!0}function j(e){e.target===document&&(document.scrollingElement.scrollTop=document.scrollingElement.scrollTop)}function _(e){C!==!0&&(C=!0,requestAnimationFrame(()=>{C=!1;const{height:t}=e.target,{clientHeight:l,scrollTop:o}=document.scrollingElement;(q===void 0||t!==window.innerHeight)&&(q=l-t,document.scrollingElement.scrollTop=o),o>q&&(document.scrollingElement.scrollTop-=Math.ceil((o-q)/8))}))}function z(e){const t=document.body,l=window.visualViewport!==void 0;if(e==="add"){const{overflowY:o,overflowX:i}=window.getComputedStyle(t);V=ie(window),P=ne(window),$=t.style.left,U=t.style.top,W=window.location.href,t.style.left=`-${V}px`,t.style.top=`-${P}px`,i!=="hidden"&&(i==="scroll"||t.scrollWidth>window.innerWidth)&&t.classList.add("q-body--force-scrollbar-x"),o!=="hidden"&&(o==="scroll"||t.scrollHeight>window.innerHeight)&&t.classList.add("q-body--force-scrollbar-y"),t.classList.add("q-body--prevent-scroll"),document.qScrollPrevented=!0,w.is.ios===!0&&(l===!0?(window.scrollTo(0,0),window.visualViewport.addEventListener("resize",_,m.passiveCapture),window.visualViewport.addEventListener("scroll",_,m.passiveCapture),window.scrollTo(0,0)):window.addEventListener("scroll",j,m.passiveCapture))}w.is.desktop===!0&&w.is.mac===!0&&window[`${e}EventListener`]("wheel",re,m.notPassive),e==="remove"&&(w.is.ios===!0&&(l===!0?(window.visualViewport.removeEventListener("resize",_,m.passiveCapture),window.visualViewport.removeEventListener("scroll",_,m.passiveCapture)):window.removeEventListener("scroll",j,m.passiveCapture)),t.classList.remove("q-body--prevent-scroll"),t.classList.remove("q-body--force-scrollbar-x"),t.classList.remove("q-body--force-scrollbar-y"),document.qScrollPrevented=!1,t.style.left=$,t.style.top=U,window.location.href===W&&window.scrollTo(V,P),q=void 0)}function ue(e){let t="add";if(e===!0){if(g++,b!==null){clearTimeout(b),b=null;return}if(g>1)return}else{if(g===0||(g--,g>0))return;if(t="remove",w.is.ios===!0&&w.is.nativeMobile===!0){b!==null&&clearTimeout(b),b=setTimeout(()=>{z(t),b=null},100);return}}z(t)}function qe(){let e;return{preventBodyScroll(t){t!==e&&(e!==void 0||t===!0)&&(e=t,ue(t))}}}function ke(){let e=null;const t=B();function l(){e!==null&&(clearTimeout(e),e=null)}return O(l),D(l),{removeTimeout:l,registerTimeout(o,i){l(),te(t)===!1&&(e=setTimeout(()=>{e=null,o()},i))}}}function Le(){if(window.getSelection!==void 0){const e=window.getSelection();e.empty!==void 0?e.empty():e.removeAllRanges!==void 0&&(e.removeAllRanges(),G.is.mobile!==!0&&e.addRange(document.createRange()))}else document.selection!==void 0&&document.selection.empty()}function Te(e,t,l){return l<=t?t:Math.min(l,Math.max(t,e))}function Se(e,t,l){if(l<=t)return t;const o=l-t+1;let i=t+(e-t)%o;return i<t&&(i=o+i),i===0?0:i}var Ee=x({name:"QItemSection",props:{avatar:Boolean,thumbnail:Boolean,side:Boolean,top:Boolean,noWrap:Boolean},setup(e,{slots:t}){const l=d(()=>`q-item__section column q-item__section--${e.avatar===!0||e.side===!0||e.thumbnail===!0?"side":"main"}`+(e.top===!0?" q-item__section--top justify-start":" justify-center")+(e.avatar===!0?" q-item__section--avatar":"")+(e.thumbnail===!0?" q-item__section--thumbnail":"")+(e.noWrap===!0?" q-item__section--nowrap":""));return()=>k("div",{class:l.value},H(t.default))}}),_e=x({name:"QItem",props:{...F,...le,tag:{type:String,default:"div"},active:{type:Boolean,default:null},clickable:Boolean,dense:Boolean,insetLevel:Number,tabindex:[String,Number],focused:Boolean,manualFocus:Boolean},emits:["click","keyup"],setup(e,{slots:t,emit:l}){const{proxy:{$q:o}}=B(),i=X(e,o),{hasLink:f,linkAttrs:r,linkClass:s,linkTag:c,navigateOnClick:L}=oe(),u=Q(null),p=Q(null),y=d(()=>e.clickable===!0||f.value===!0||e.tag==="label"),v=d(()=>e.disable!==!0&&y.value===!0),h=d(()=>"q-item q-item-type row no-wrap"+(e.dense===!0?" q-item--dense":"")+(i.value===!0?" q-item--dark":"")+(f.value===!0&&e.active===null?s.value:e.active===!0?` q-item--active${e.activeClass!==void 0?` ${e.activeClass}`:""}`:"")+(e.disable===!0?" disabled":"")+(v.value===!0?" q-item--clickable q-link cursor-pointer "+(e.manualFocus===!0?"q-manual-focusable":"q-focusable q-hoverable")+(e.focused===!0?" q-manual-focusable--focused":""):"")),T=d(()=>{if(e.insetLevel===void 0)return null;const a=o.lang.rtl===!0?"Right":"Left";return{["padding"+a]:16+e.insetLevel*56+"px"}});function S(a){v.value===!0&&(p.value!==null&&(a.qKeyEvent!==!0&&document.activeElement===u.value?p.value.focus():document.activeElement===p.value&&u.value.focus()),L(a))}function E(a){if(v.value===!0&&J(a,[13,32])===!0){K(a),a.qKeyEvent=!0;const M=new MouseEvent("click",a);M.qKeyEvent=!0,u.value.dispatchEvent(M)}l("keyup",a)}function n(){const a=Z(t.default,[]);return v.value===!0&&a.unshift(k("div",{class:"q-focus-helper",tabindex:-1,ref:p})),a}return()=>{const a={ref:u,class:h.value,style:T.value,role:"listitem",onClick:S,onKeyup:E};return v.value===!0?(a.tabindex=e.tabindex||"0",Object.assign(a,r.value)):y.value===!0&&(a["aria-disabled"]="true"),k(c.value,a,n())}}});export{_e as Q,he as a,ke as b,Le as c,ge as d,we as e,Te as f,qe as g,Ee as h,be as i,pe as j,Se as n,ye as u};