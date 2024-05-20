import{a as f,Q as b}from"./QCard.246add5a.js";import{Q as _}from"./QInput.283eb062.js";import{c as w,d as g,h as i,g as q,A as y,Z as B,B as m,C,D as r,F as s,L as h,G as v,K as l,a as k}from"./index.4c705956.js";import{u as Q,a as S}from"./use-dark.371bb89c.js";import{h as p}from"./render.9b0eaa5f.js";import{a as V}from"./QBtn.e9a2bcf7.js";import{Q as I}from"./QPage.fb1668d3.js";import"./dom.b5015e69.js";var x=w({name:"QBanner",props:{...Q,inlineActions:Boolean,dense:Boolean,rounded:Boolean},setup(o,{slots:c}){const{proxy:{$q:e}}=q(),d=S(o,e),u=g(()=>"q-banner row items-center"+(o.dense===!0?" q-banner--dense":"")+(d.value===!0?" q-banner--dark q-dark":"")+(o.rounded===!0?" rounded-borders":"")),n=g(()=>`q-banner__actions row items-center justify-end col-${o.inlineActions===!0?"auto":"all"}`);return()=>{const t=[i("div",{class:"q-banner__avatar col-auto row items-center self-start"},p(c.avatar)),i("div",{class:"q-banner__content col text-body2"},p(c.default))],a=p(c.action);return a!==void 0&&t.push(i("div",{class:n.value},a)),i("div",{class:u.value+(o.inlineActions===!1&&a!==void 0?" q-banner--top-padding":""),role:"alert"},t)}}});const A=l("img",{height:"300px",src:"https://img.freepik.com/free-photo/packings-of-pills-and-capsules-of-medicines_1339-2254.jpg"},null,-1),E=l("div",{class:"text-h6"},'\u041E\u041E\u041E "\u0417\u0434\u043E\u0440\u043E\u0432\u044C\u0435"',-1),z=l("div",{class:"text-subtitle2"},"\u0410\u0434\u043C\u0438\u043D\u0438\u0441\u0442\u0440\u0430\u0442\u0438\u0432\u043D\u0430\u044F \u043F\u0430\u043D\u0435\u043B\u044C",-1),D={key:0,class:"q-my-md text-center"},P=l("div",{class:"text-h6"},"\u041E\u0448\u0438\u0431\u043A\u0430 \u0430\u0432\u0442\u043E\u0440\u0438\u0437\u0430\u0446\u0438\u0438",-1),$={key:1,class:"q-my-md text-center"},j=l("div",{class:"text-h6"},"\u0423\u0441\u043F\u0435\u0448\u0435\u043D\u0430\u044F \u0430\u0432\u0442\u043E\u0440\u0438\u0437\u0430\u0446\u0438\u044F",-1),L={class:"q-pa-md column"},Z=Object.assign({name:"LoginPage"},{__name:"LoginPage",setup(o){const c=y(),e=B({login:"",pwd:"",mistakeStatus:!1,successEnter:!1}),d={headers:{"Content-Type":"application/x-www-form-urlencoded"}};function u(){k.post("https://zdorovie.space/api/v1/token",{username:e.login,password:e.pwd},d).then(function(n){e.mistakeStatus=!1,e.successEnter=!0,localStorage.setItem("access_token",n.data.access_token),k.get("https://zdorovie.space/api/v1/users/me/",{headers:{Authorization:`Bearer ${localStorage.getItem("access_token")}`}}).then(t=>{localStorage.setItem("username",t.data.username),localStorage.setItem("role",t.data.role)}),c.push({name:"Order"})}).catch(function(n){console.log(n),console.log("\u043E\u0448\u0438\u0431\u043A\u0430 \u0430\u0432\u0442\u043E\u0440\u0438\u0437\u0430\u0446\u0438\u0438"),e.successEnter=!1,e.mistakeStatus=!0})}return(n,t)=>(m(),C(I,{class:"flex flex-center"},{default:r(()=>[s(b,{class:"my-card"},{default:r(()=>[A,s(f,null,{default:r(()=>[E,z]),_:1}),s(f,null,{default:r(()=>[s(_,{modelValue:e.login,"onUpdate:modelValue":t[0]||(t[0]=a=>e.login=a),type:"text",label:"\u041B\u043E\u0433\u0438\u043D"},null,8,["modelValue"]),s(_,{modelValue:e.pwd,"onUpdate:modelValue":t[1]||(t[1]=a=>e.pwd=a),type:"password",label:"\u041F\u0430\u0440\u043E\u043B\u044C"},null,8,["modelValue"]),e.mistakeStatus?(m(),h("div",D,[s(x,{"inline-actions":"",class:"text-white bg-red"},{default:r(()=>[P]),_:1})])):v("",!0),e.successEnter?(m(),h("div",$,[s(x,{"inline-actions":"",class:"text-white bg-green"},{default:r(()=>[j]),_:1})])):v("",!0),l("div",L,[s(V,{size:"md",color:"primary",label:"\u0412\u043E\u0439\u0442\u0438",onClick:t[2]||(t[2]=a=>u())})])]),_:1})]),_:1})]),_:1}))}});export{Z as default};
