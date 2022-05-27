let select_UT = document.getElementById('id_utilizacao_Tipo')
let form_container = document.getElementById("form_container")
let count = 0
let counterAmb = 0

//Execução principal

select_UT.addEventListener('change', () =>{
    clear(1)
    createDiv('formStep', form_container)
    insertFields(select_UT.value)//segundo nivel
    //craeteInputSubmit()
})

function createDiv(idName, parent, classe= 0, tag=''){
    let component = document.createElement('div')
    component.setAttribute('id', idName)
    component.className = 'form-group'
    if (classe == 1){
        component.classList.add('formStep_amb')
    }else if (classe == 2){
        component.classList.add('formStep_amb')
        component.classList.add(tag)
    }
 
    parent.appendChild(component)
}


function set_label(target, msg){
    let elemento = document.createElement('label')
    elemento.setAttribute('for', target)
    elemento.textContent = msg

    return elemento
}


function add_Field(fieldName, id_field, msg_label, step=1, apender = '', indexMat= null){
    //nome campo, id do campo, mensagem a exibir no label, etapa que o campo está inserido
    let componente = document.createElement("div")
    componente.className = "form-group"
    componente.setAttribute('id', 'form_id_' + fieldName)
    let divLabel = document.createElement('div')
    divLabel.className = "col-12"
    divLabel.appendChild(set_label(id_field, msg_label))

    let divField = document.createElement('div')
    //divField.className = "col-auto"
    divField.innerHTML += fields[fieldName]
    
    componente.appendChild(divLabel)
    componente.appendChild(divField)
    
    //Alterações inputs recebidos
    /*if (fields[fieldName]){
        console.log(divField.children[0].nodeName)
    }*/
    if (divField.children[0].nodeName == 'SELECT'){
        divField.children[0].className = 'form-select'
        
        if (['ar_Livre', 'local_Risco_D', 'local_Risco_E'].indexOf(divField.children[0].attributes[0].nodeValue) != -1){
            divField.className = "col-3"
        }else if (divField.children[0].attributes[0].nodeValue == 'finalidade'){
            divField.className = "col-4"
            //componente.children[1].classList.add('form-control')
        }else if (divField.children[0].attributes[0].nodeValue == 'material'){
            divField.className = "col-8"
            //componente.children[1].classList.add('form-control')
        }

    }else if (divField.children[0].nodeName == 'INPUT'){
        divField.children[0].className = 'form-control'
        if (divField.children[0].attributes[0].nodeValue == 'number'){
            divField.className = "col-3"
            
        }else if (divField.children[0].attributes[0].nodeValue == 'text'){
            divField.className = "col-3"
        }
    }
    
    
    let box = document.getElementById('formStep')

    if (step == 1){
        if (document.getElementById('formStep_1')){
            document.getElementById("formStep_1").appendChild(componente)
            return
        }
        createDiv('formStep_1', box )
        document.getElementById("formStep_1").appendChild(componente)

    }else if (step == 2){
        if (document.getElementById('formStep_2')){
            document.getElementById("formStep_2").appendChild(componente)
            return
        }
        createDiv('formStep_2', box )
        document.getElementById("formStep_2").appendChild(componente)
    }
    else if (step == 3){
        let id_dinamico = 'formStep_amb_' + counterAmb //id container

        if (document.getElementById(id_dinamico)){
            let newId = 'id_finalidade_' + counterAmb //id select material
            document.getElementById(id_dinamico).appendChild(componente)
            document.getElementById('id_finalidade').setAttribute('id', newId)
            
            return [newId, id_dinamico, counterAmb]
        }

        createDiv(id_dinamico, document.getElementById('formStep_1'), 1)
        document.getElementById(id_dinamico).appendChild(componente)

    }else if (step == 4){
        //let id_dinamico = 'formStep_amb_' + counterAmb

        //apender.appendChild(componente)
        document.getElementById(apender).appendChild(componente)//appendChild(componente)
    }
    
}

function craeteInputSubmit() {
    var inputSubmit = document.createElement('input')
    inputSubmit.className = "btn btn-primary btn-block"
    inputSubmit.setAttribute('id', 'bt_Submit')
    inputSubmit.setAttribute('type', 'submit')
    inputSubmit.setAttribute('value', 'Verificar Categoria')
    
    if (document.getElementById("bt_Submit")){
        return
    }

    createDiv('formControl', document.getElementById('formStep'))
    let container = document.getElementById('formControl')
    container.classList = "col-7 mx-auto"
    container.appendChild(inputSubmit)
}

function clear(target) {
    if (target == 1){
        let formStep = document.getElementById('formStep')
        if(formStep){
            formStep.remove()
            count = 0
        }
    }else if (target == 2){
        if (document.getElementById('formStep_2')){
            document.getElementById('formStep_2').innerHTML = ''
        }
    }
   

}

function dinamico_Efetivo_Local_D(){
    let eventoRisco_D = document.getElementById("id_local_Risco_D")
    eventoRisco_D.addEventListener("change", () =>{
        if (eventoRisco_D.value == 'yes'){
            clear(2)
            add_Field('efetivo_Local_D', "id_efetivo_Local_D", "Informe o efetivo do local D", 2)
            craeteInputSubmit()
            return
        }
        clear(2)
        craeteInputSubmit()
    })
}

function dinamico_Efetivo_Local_E(){
    let eventoRisco_E = document.getElementById("id_local_Risco_E")
    eventoRisco_E.addEventListener("change", () =>{
        if (eventoRisco_E.value == 'yes'){
            clear(2)
            add_Field('efetivo_Local_E', "id_efetivo_Local_E", "Informe o efetivo do local E", 2)
            craeteInputSubmit()
            return
        }
        clear(2)
        craeteInputSubmit()
    })
}

function dinamico_Altura_Subsolo_Area(){
    let eventoArlivre = document.getElementById("id_ar_Livre")
    eventoArlivre.addEventListener("change", () =>{
        if (eventoArlivre.value == 'no'){
            clear(2)
            add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:", 2)
            add_Field('subsolo',"id_subsolo", "Informe o número de pisos abaixo da referencia:", 2)
            add_Field('area_Bruta', "id_area_Bruta", "Insira a área bruta ocupada pelo estabelecimento em m²:",2)
            craeteInputSubmit()
            return
        }
        clear(2)
        add_Field('area_Bruta', "id_area_Bruta", "Informe a área bruta ocupara pelo estabelecimento:", 2)
        craeteInputSubmit()
    })
}

function dinamico_Altura_Subsolo_Efetivo(){
    let eventoArlivre = document.getElementById("id_ar_Livre")
    eventoArlivre.addEventListener("change", () =>{
        if (eventoArlivre.value == 'no'){
            clear(2)
            add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:", 2)
            add_Field('subsolo',"id_subsolo", "Informe o número de pisos abaixo da referencia:", 2)
            add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:", 2)
            craeteInputSubmit()
            return
        }
        clear(2)
        add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:", 2)
        craeteInputSubmit()
    })
}

function add_ambiente(){
    
    let container = document.getElementById('formStep_1')
    let bt_add = document.createElement("button")
    lbl = document.createTextNode("Insira ambientes existente no edificio dedicado a fabricação, manutenção, manipulação ou armazenamento e preencha os dados:")
    container.appendChild(lbl)
    bt_add.className = 'form-button'
    bt_add.setAttribute("id", "id_bt_add")
    bt_add.innerText = 'Incluir novo ambiente'

    bt_add.onclick = () =>{

        add_Field('ambiente_Nome',"id_nome_Ambiente", "Informe o nome do ambiente:", 3)
        //add_Field('areaAmbiente',"id_Area_Ambiente", "Informe a área em m² do ambiente :", 2)
        let id = add_Field('finalidade',"id_finalidade", "Qual a destinação do ambiente:", 3)
        tipoFinalidade(id)
        //btAddMaterial(id)
        btDelete(id)
        
        window['material_amb_' + counterAmb] = 0
        
        
        counterAmb ++
    }

    container.appendChild(bt_add)
}

function tipoFinalidade(target){
    
    let componente = document.getElementById(target[0])

    componente.addEventListener('change', () =>{
        
        if (componente.value == 'Armazenamento'){
            clearLote(target[1])
            setMaterial(target)

        }else{
        clearLote(target[1])
        setMaterial(target, false)}
        btAddMaterial(target)    
    })

}

function clearLote(tag){
    /*função encarregada de excluir uma lista de elementos.
    tag = recebe o nome da classe a excluir*/
    let list = document.getElementsByClassName(tag)
            for (let i = list.length - 1; i>= 0; i --){
                list[i].remove()
            }
}


function btAddMaterial(parent){
    let btAddMaterial = document.createElement("button")
    btAddMaterial.setAttribute("id", "id_addMaterial_" + parent[2])
    btAddMaterial.className = "form-button"
    btAddMaterial.innerText = 'Novo Material'
    document.getElementById(parent[1]).appendChild(btAddMaterial)

    btAddMaterial.addEventListener('click', () =>{
        setMaterial(parent)
    })
}

function setMaterial(config, armazen=true){
    let idDivMat = 'material_amb_' + config[2] +'_' + eval('material_amb_' + config[2])
    if (armazen){
        createDiv(idDivMat, document.getElementById(config[1]), 2, config[1])
        add_Field('materiais',"id_material", "Indique material ou substâncias relacionados ao ambiente:", 4, apender= idDivMat)
        add_Field('volume',"id_volume", "volume máximo de material m³:", 4, apender= idDivMat)
        btDeleteMat(idDivMat)
        eval('material_amb_' + config[2] + ' ++')
    }else{
        createDiv(idDivMat, document.getElementById(config[1]), 2, config[1])
        add_Field('materiais',"id_material", "Indique material ou substâncias relacionados ao ambiente:", 4, apender= idDivMat)
        btDeleteMat(idDivMat)
        eval('material_amb_' + config[2] + ' ++')
    }
}

function btDelete(id){
    let btDelete = document.createElement("button")
    btDelete.setAttribute("id", "id_bt_delete_" + id[2])
    btDelete.className = 'form-button'
    btDelete.innerText = 'Excluir ambiente'
    btDelete.addEventListener('click', () =>{
        btDelete.parentElement.remove()
    })
    
    document.getElementById("formStep_amb_" + counterAmb).appendChild(btDelete)
}

function btDeleteMat(parent){
    let btDelete = document.createElement("button")
    btDelete.setAttribute("id", parent + "_Del")
    btDelete.className = 'form-button'
    btDelete.innerText = 'Excluir Material'
    document.getElementById(parent).appendChild(btDelete)
    
    btDelete.addEventListener('click', () =>{
        btDelete.parentElement.remove()
    })
}

let labelAltura = "Insira a altura do estabelecimento em metros:"
let labelSubsolo = "Insira o número de pisos ocupados pelo edifício abaixo do plano de referência:"

function insertFields(valor){
    switch (valor){
        case "1":
            add_Field('altura',"id_altura", labelAltura)
            add_Field('subsolo',"id_subsolo", labelSubsolo)
            craeteInputSubmit()
            break
        case "2":
            add_Field('ar_Livre', "id_ar_Livre", "Estabelecimento ao ar livre", 1)
            dinamico_Altura_Subsolo_Area()
            break
        case "3":
            add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:")
            add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:")
            craeteInputSubmit()   
            break
        case "4":
            add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:", 1)
            add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:", 1)
            add_Field('local_Risco_D', "id_local_Risco_D", "Existe local de risco D no estabelecimento", 1) 
            dinamico_Efetivo_Local_D()
            break
        case "5":
            add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:", 1)
            add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:", 1)
            add_Field('local_Risco_D', "id_local_Risco_D", "Existe local de risco D no estabelecimento", 1)
            dinamico_Efetivo_Local_D()        
            break
        case "6":
            add_Field('ar_Livre', "id_ar_Livre", "Estabelecimento ao ar livre?", 1)
            dinamico_Altura_Subsolo_Efetivo()
            break
        case "7":
            add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:", 1)
            add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:", 1)
            add_Field('local_Risco_E', "id_local_Risco_E", "Existe local de risco E no estabelecimento", 1)
            dinamico_Efetivo_Local_E()
            break
        case "8":
            add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:", 1)
            add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:", 1)
            add_Field('subsolo',"id_subsolo", "Informe o número de pisos abaixo da referencia:", 1)
            craeteInputSubmit()
            break
        case "9":
            add_Field('ar_Livre', "id_ar_Livre", "Estabelecimento ao ar livre?", 1)
            dinamico_Altura_Subsolo_Efetivo()
            break
        case "10":
            add_Field('ar_Livre', "id_ar_Livre", "Estabelecimento ao ar livre?", 1)
            dinamico_Altura_Subsolo_Efetivo()
            break
        case "11":
            /*add_Field('altura',"id_altura", "Informe a altura do piso mais elevado do estabelecimento:", 1)
            add_Field('efetivo', "id_efetivo", "Informe o efetivo total do estabelecimento:", 1)
            add_Field('subsolo',"id_subsolo", "Informe o número de pisos abaixo da referencia:", 1)
            add_ambiente()*/
            //step 3 - calculo carga de incêndio
            window.alert("Opção indisponivel")
            break
        case "12":
            /*add_Field('ar_Livre', "id_ar_Livre", "Estabelecimento ao ar livre?", 1)
            add_Field('subsolo',"id_subsolo", "Informe o número de pisos abaixo da referencia:", 1)*/
            window.alert("Opção indisponivel")
            break
      
    }

}
