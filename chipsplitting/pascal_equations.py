# def varphi_hat(degree, i):
#     assert degree >= 11, "degree must be greater or equal than 11"
#     assert i >= 1 and i <= 3 or i >= degree - 3 and i <= degree - 1, "i must lie between 1<=i<=3 or degree-3<=i<=degree-1"

#     support_neg = np.full(16 * 3 + 16, False)
#     support_x_pos, support_y_pos, support_z_pos = np.full(16, False), np.full(16, False), np.full(16, False)
#     support_b_pos, support_c_pos, support_d0_pos, support_d1_pos = np.full(4, False), np.full(4, False), np.full(4, False), np.full(4, False)
        
#     if i >= 1 and i <= 3:
#         # x support
#         support_x_pos[:4 + (4 * i)] = True
        
#         # y support
#         for col in range(i+1):
#             for index in range(4*col, 4*(col+1)-i+col):
#                 support_y_pos[index] = True
                
#         # c support
#         support_c_pos[:i+1] = True
        
#         return np.concatenate([support_x_pos, support_y_pos, support_z_pos, support_b_pos, support_c_pos, support_d0_pos, support_d1_pos]), support_neg
#     elif i >= degree - 3 and degree <= degree - 1:
#          # x support
#         support_x_pos[:4 + (4 * i)] = True
#         return np.concatenate([support_x_pos, support_y_pos, support_z_pos, support_b_pos, support_c_pos, support_d0_pos, support_d1_pos]), support_neg
#     else:
#         raise NotImplementedError

# -------------------------
# PSI
# -------------------------

PSI_HAT_1_SUPP = (
  [
    # x
    False,  True,  False,  False,  
    False,  True,  False,  False, 
    False,  True,  False,  False, 
    False,  True,  False,  False, 
    # y
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    False, True, False, False,
    False, True, False, False, 
    False, True, False, False, 
    False, True, False, False, 
    # b
    False, True, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    True,  False,  False,  False, 
    True,  False,  False,  False, 
    True,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    True, False, False, False,
    True, False, False, False, 
    True, False, False, False, 
    True, False, False, False, 
    # b
    True, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ]
)

PSI_HAT_2_SUPP = (
  [
    # x
    False,  False,  True,  False,  
    False,  False,  True,  False, 
    True,  False,  True,  False, 
    True,  False,  True,  False, 
    # y
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    True, False, True, False,
    True, False, True, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    True, False, True, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  True,  False,  False, 
    False,  True,  False,  False, 
    False,  True,  False,  False, 
    # y
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    False, True, False, False,
    False, True, False, False, 
    False, True, False, False, 
    False, True, False, False, 
    # b
    False, True, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ]
)

PSI_HAT_3_SUPP = (
  [
    # x
    False,  False,  False,  True,  
    False,  False,  False,  True, 
    False,  True,  False,  True, 
    False,  True,  False,  True, 
    # y
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    False, True, False, True,
    False, True, False, True, 
    False, True, False, True, 
    False, True, False, True, 
    # b
    False, True, False, True,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  True,  False, 
    False,  False,  True,  False, 
    True,  False,  True,  False, 
    # y
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    True, False, True, False,
    True, False, True, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    True, False, True, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ]
)

PSI_HAT_4_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    True,   True,  True,  True, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    True,  True,  True,  True, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    False,  True, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ],
  [
    # x
    False,  True,  True,  True,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    True, True, True, True, 
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    True,  False, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ]
)

PSI_HAT_5_SUPP = (
  [
    # x
    False,  False,  True,   True,  
    False,  False,  False,  False, 
    True,   True,   True,   True, 
    False,  False,  False,  False, 
    # y
    True,   True, True, True, 
    False,  False,  False,  False, 
    True,   True,   True,  True, 
    False,  False,  False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    True,  False, True, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  True,  True,  True, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    True, True, True, True, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    False,  True, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ]
)

PSI_HAT_6_SUPP = (
  [
    # x
    False,  False,  False,   False,  
    False,  False,  True,  True, 
    False,   False,   False,   False, 
    True,  True,  True,  True, 
    # y
    False,   False, False, False, 
    True,  True,  True,  True, 
    False,   False,   False,  False, 
    True,  True,  True, True, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    False,  True, False, True, 
    # d
    False, False, False, False,
    False, False, False, False
  ],
  [
    # x
    False,  False,  False,  True,  
    False,  False,  False,  False, 
    False,  True,  True,  True, 
    False,  False,  False,  False, 
    # y
    True, True, True, True, 
    False, False, False, False, 
    True, True, True, True, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    True,  False, True, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ]
)


# -------------------------
# XI
# -------------------------

XI_HAT_1_EVEN_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, True, False, 
    False, False, False, True, 
    False, False, True, False, 
    False, False, False, True, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, True, False, True, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, True, False, False,
    True, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, False, True, False, 
    False, False, False, True, 
    False, False, True, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, False, False, False,
    False, True, False, False
  ]
)

XI_HAT_1_ODD_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, True, False, 
    False, False, False, True, 
    False, False, True, False, 
    False, False, False, True, 
    # z
    False, False, False, False,
    False, False, False, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, True, False, False,
    True, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, False, True, False, 
    False, False, False, True, 
    False, False, True, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, True, False, True, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, False, False, False,
    False, True, False, False
  ]
)

XI_HAT_2_EVEN_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, True, False, False, 
    False, False, True, False, 
    False, True, False, True, 
    False, False, True, False, 
    # z
    False, False, False, False,
    True, False, True, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, False, True, False,
    False, True, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, True, False, False, 
    False, False, True, False, 
    False, True, False, True, 
    # z
    False, False, False, False,
    False, True, False, True, 
    False, True, False, True, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, True, False, False,
    True, False, True, False
  ]
)

XI_HAT_2_ODD_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, True, False, False, 
    False, False, True, False, 
    False, True, False, True, 
    False, False, True, False, 
    # z
    False, False, False, False,
    False, True, False, True, 
    False, True, False, True, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, False, True, False,
    False, True, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, True, False, False, 
    False, False, True, False, 
    False, True, False, True, 
    # z
    False, False, False, False,
    True, False, True, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, True, False, False,
    True, False, True, False
  ]
)

XI_HAT_3_EVEN_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    True, False, False, False, 
    False, True, False, False, 
    True, False, True, False, 
    False, True, False, True, 
    # z
    False, True, False, True,
    False, True, False, True, 
    False, True, False, True, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, True, False, True,
    True, False, True, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    True, False, False, False, 
    False, True, False, False, 
    True, False, True, False, 
    # z
    True, False, True, False,
    True, False, True, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, False, True, False,
    False, True, False, True
  ]
)

XI_HAT_3_ODD_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    True, False, False, False, 
    False, True, False, False, 
    True, False, True, False, 
    False, True, False, True, 
    # z
    True, False, True, False,
    True, False, True, False, 
    True, False, True, False, 
    True, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, True, False, True,
    True, False, True, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    True, False, False, False, 
    False, True, False, False, 
    True, False, True, False, 
    # z
    False, True, False, True,
    False, True, False, True, 
    False, True, False, True, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, False, True, False,
    False, True, False, True
  ]
)

XI_HAT_4_EVEN_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, False, True, True, 
    False, False, False, False, 
    False, False, True, True, 
    # z
    False, False, False, False,
    False, False, False, False, 
    True, False, True, False, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    True, True, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, True, True, 
    False, False, False, False, 
    False, False, True, True, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, True, False, True, 
    False, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, True, False, False,
    False, False, False, False
  ]
)

XI_HAT_4_ODD_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, True, True, 
    False, False, False, False, 
    False, False, True, True, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    True, False, True, False, 
    False, True, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, True, False, False,
    False, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, False, True, True, 
    False, False, False, False, 
    False, False, True, True, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, True, False, True, 
    False, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    True, True, False, False,
  ]
)

XI_HAT_5_EVEN_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, True, True, True, 
    False, False, False, False, 
    False, True, True, True, 
    False, False, False, False, 
    # z
    False, False, False, False,
    True, False, True, False, 
    False, True, False, True, 
    False, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, True, True, False,
    False, False, False, False
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, True, True, True, 
    False, False, False, False, 
    False, True, True, True, 
    # z
    False, False, False, False,
    False, True, False, True, 
    False, False, True, False, 
    False, False, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    True, True, True, False
  ]
)

XI_HAT_5_ODD_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    False, True, True, True, 
    False, False, False, False, 
    False, True, True, True, 
    # z
    False, False, False, False,
    True, False, True, False, 
    False, True, False, True, 
    False, False, True, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    True, True, True, False,
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, True, True, True, 
    False, False, False, False, 
    False, True, True, True, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, True, False, True, 
    False, False, True, False, 
    False, False, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, True, True, False,
    False, False, False, False,
  ]
)

XI_HAT_6_EVEN_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    True, True, True, True, 
    False, False, False, False, 
    True, True, True, True, 
    # z
    True, False, True, False,
    False, True, False, True, 
    False, False, True, False, 
    False, False, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    True, True, True, True
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    True, True, True, True, 
    False, False, False, False, 
    True, True, True, True, 
    False, False, False, False, 
    # z
    False, True, False, True,
    False, False, True, False, 
    False, False, False, True, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, True, True, True,
    False, False, False, False
  ]
)

XI_HAT_6_ODD_SUPP = (
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    True, True, True, True, 
    False, False, False, False, 
    True, True, True, True, 
    False, False, False, False, 
    # z
    True, False, True, False,
    False, True, False, True, 
    False, False, True, False, 
    False, False, False, True, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    True, True, True, True,
    False, False, False, False,
  ],
  [
    # x
    False,  False,  False,  False,  
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    False,  False,  False,  False, 
    # y
    False, False, False, False, 
    True, True, True, True, 
    False, False, False, False, 
    True, True, True, True, 
    # z
    False, True, False, True,
    False, False, True, False, 
    False, False, False, True, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    False,  False, False, False, 
    # d
    False, False, False, False,
    True, True, True, True
  ]
)

# -------------------------
# PHI
# -------------------------

PHI_HAT_1_SUPP = (
  [
    # x
    True,  True,  True,  True,  
    True,  True,  True,  True, 
    False, False, False, False, 
    False, False, False, False,  
    # y
    True,  True, True, False,  
    True,  True, True, True, 
    False, False, False, False, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    True,  True, False, False, 
    # d
    False, False, False, False,
    False, False, False, False
  ],
  [
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False
  ]
)

PHI_HAT_2_SUPP = (
  [
    # x
    True,  True,  True,  True,  
    True,  True,  True,  True,  
    True,  True,  True,  True, 
    False, False, False, False,  
    # y
    True,  True, False, False,  
    True,  True,  True, False,  
    True,  True,  True, True, 
    False, False, False, False, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False, 
    # c
    True,  True, True, False, 
    # d
    False, False, False, False, 
    False, False, False, False
  ],
  [
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False
  ]
)

PHI_HAT_3_SUPP = (
  [
    # x
    True,  True,  True,  True,  
    True,  True,  True,  True,  
    True,  True,  True,  True,  
    True,  True,  True,  True,  
    # y
    True, False, False, False,  
    True,  True, False, False, 
    True,  True,  True, False,  
    True,  True,  True,  True, 
    # z
    False, False, False, False,
    False, False, False, False, 
    False, False, False, False, 
    False, False, False, False, 
    # b
    False, False, False, False,  
    # c
    True,  True, True,  True,
    # d
    False, False, False, False, 
    False, False, False, False
  ],
  [
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False
  ]
)

PHI_HAT_4_SUPP = (
  [
    # x
    True,  True,  False,  False,  
    True,  True,  False,  False,  
    True,  True,  False,  False,  
    True,  True,  False,  False,  
    # y
    False, False, False,  False,  
    False, False, False,  False,  
    False, False, False,  False,  
    False, False, False,  False, 
    # z
    True,  True,  False,  False, 
    True,  True,  False,  False, 
    True,  True,  False,  False, 
    False, True,  False,  False,  
    # b
    True,  True,  False,   False, 
    # c
    False, False, False,  False, 
    # d
    False, False, False,  False,
    False, False, False,  False,
  ],
  [
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False
  ]
)

PHI_HAT_5_SUPP = (
  [
    # x
    True,  True,  True,  False,  
    True,  True,  True,  False,  
    True,  True,  True,  False,  
    True,  True,  True,  False,  
    # y
    False, False, False,  False,  
    False, False, False,  False,  
    False, False, False,  False,  
    False, False, False,  False, 
    # z
    True,  True,  True,  False, 
    True,  True,  True,  False, 
    False, True,  True,  False, 
    False, False,  True,  False,  
    # b
    True,  True,  True,   False, 
    # c
    False, False, False,  False, 
    # d
    False, False, False,  False,
    False, False, False,  False,
  ],
  [
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False
  ]
)

PHI_HAT_6_SUPP = (
  [
    # x
    True,  True,  True,  True,  
    True,  True,  True,  True,  
    True,  True,  True,  True,  
    True,  True,  True,  True,  
    # y
    False, False, False,  False,  
    False, False, False,  False,  
    False, False, False,  False,  
    False, False, False,  False, 
    # z
    True,  True,  True,  True, 
    False,  True,  True,  True, 
    False, False,  True,  True, 
    False, False,  False,  True,  
    # b
    True,  True,  True,   True, 
    # c
    False, False, False,  False, 
    # d
    False, False, False,  False,
    False, False, False,  False,
  ],
  [
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False,
    False
  ]
)