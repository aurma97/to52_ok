import api from '@/services/api'

const config = {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
}

export default {
  fetchEquipments() {
    return api.get(`equipments/`)
              .then(response => response.data)
  },
  showEquipment(id) {
    return api.get(`equipments/show/${id}`)
              .then(response => response.data)
  },
  postEquipment(payload) {
    return api.post(`equipments/create`, payload)
              .then(response => response.data)

  },
  updateEquipment(payload) {
    return api.put(`equipments/update-or-delete/${payload.id}`, payload)
              .then(response => response.data)
              .catch(function (error) {
               
              })
  },
  deleteEquipment(id) {
    return api.delete(`equipments/update-or-delete/${id}`)
              .then(response => { 
                
              })  
  }
}