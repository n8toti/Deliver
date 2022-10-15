from Deliver import Graph, Vertex
class Data:

    def __init__(self):
        data = []
    
    def data(self):
        data = [[1, "195 W Oakland Ave", "10:30 AM", "Salt Lake City", 84115,	21, "at the hub"],
        [2,	"2530 S 500 E",	"EOD", "Salt Lake City", 84106, 44, "at the hub"],
        [3,	"233 Canyon Rd", "EOD", "Salt Lake City", 84103, 2, "at the hub"],
        [4,	"380 W 2880 S",	"EOD", "Salt Lake City", 84115, 4, "at the hub"],
        [5,	"410 S State St", "EOD", "Salt Lake City", 84111, 5, "at the hub"],
        [6,	"3060 Lester St", "10:30 AM", "West Valley City", 84119, 88, "at the hub"],
        [7,	"1330 2100 S", "EOD", "Salt Lake City", 84106,	8, "at the hub"],
        [8,	"300 State St", "EOD", "Salt Lake City", 84103, 9, "at the hub"],
        [9,	"300 State St", "EOD", "Salt Lake City", 84103, 2, "at the hub"],
        [10, "600 E 900 South", "EOD", "Salt Lake City", 84105, 1, "at the hub"],
        [11, "2600 Taylorsville Blvd", "EOD", "Salt Lake City", 84118, 1, "at the hub"],
        [12, "3575 W Valley Central Station bus Loop", "EOD", "West Valley City", 84119, 1, "at the hub"],
        [13, "2010 W 500 S", "10:30 AM", "Salt Lake City", 84104, 	2, "at the hub"],
        [14, "4300 S 1300 E", "10:30 AM", "Millcreek", 84117, 	88, "at the hub"],
        [15, "4580 S 2300 E", "9:00 AM","Holladay", 84117, 4, "at the hub"],
        [16, "4580 S 2300 E", "10:30 AM", "Holladay", 84117,88, "at the hub"],
        [17, "3148 S 1100 W", "EOD", "Salt Lake City", 84119, 2, "at the hub"],
        [18, "1488 4800 S", "EOD", "Salt Lake City", 84123, 6, "at the hub"],
        [19, "177 W Price Ave",	"EOD","Salt Lake City", 84115, 37, "at the hub"],
        [20, "3595 Main St", "10:30 AM", "Salt Lake City", 84115, 37, "at the hub"],
        [21, "3595 Main St", "EOD", "Salt Lake City", 84115, 3, "at the hub"],
        [22, "6351 South 900 East", "EOD", "Murray", 84121,	2, "at the hub"],
        [23, "5100 South 2700 West", "EOD",	"Salt Lake City", 84118, 5,"at the hub"],
        [24, "5025 State St", "EOD", "Murray", 84107, 7, "at the hub"],
        [25, "5383 South 900 East #104","10:30 AM", "Salt Lake City", 84117, 7, "at the hub"],
        [26, "5383 South 900 East #104","EOD", "Salt Lake City", 84117, 25, "at the hub"],
        [27, "1060 Dalton Ave S","EOD", "Salt Lake City", 84104, 5, "at the hub"],
        [28, "2835 Main St", "EOD", "Salt Lake City", 84115, 7, "at the hub"],
        [29, "1330 2100 S", "10:30 AM",	"Salt Lake City", 84106, 2, "at the hub"],
        [30, "300 State St", "10:30 AM", "Salt Lake City", 84103, 1, "at the hub"],
        [31, "3365 S 900 W", "10:30 AM", "Salt Lake City", 84119, 1, "at the hub"],
        [32, "3365 S 900 W", "EOD",	"Salt Lake City", 84119, 1, "at the hub"],
        [33,"2530 S 500 E", "EOD", "Salt Lake City", 84106, 1, "at the hub"],
        [34, "4580 S 2300 E", "10:30 AM", "Holladay", 84117, 2, "at the hub"],
        [35, "1060 Dalton Ave S", "EOD", "Salt Lake City", 84104, 88, "at the hub"],
        [36, "2300 Parkway Blvd", "EOD", "West Valley City", 84119, 88, "at the hub"],
        [37, "410 S State St", "10:30 AM", "Salt Lake City", 84111, 2, "at the hub"],
        [38, "410 S State St", "EOD", "Salt Lake City", 84111, 9, "at the hub"],
        [39, "2010 W 500 S", "EOD",	"Salt Lake City", 84104, 9, "at the hub"],
        [40, "380 W 2880 S", "10:30 AM", "Salt Lake City", 84115, 45, "at the hub"]]

        return data

    def create_graph(self):

        g = Graph()
        vertex_hub = Vertex("HUB")
        vertex_a = Vertex("6351 South 900 East")
        vertex_b = Vertex("1060 Dalton Ave S")
        vertex_c = Vertex("1330 2100 S")
        vertex_d = Vertex("1488 4800 S")
        vertex_e = Vertex("177 W Price Ave")
        vertex_f = Vertex("195 W Oakland Ave")
        vertex_g = Vertex("2010 W 500 S")
        vertex_h = Vertex("2300 Parkway Blvd")
        vertex_i = Vertex("233 Canyon Rd")
        vertex_j = Vertex("2530 S 500 E")
        vertex_k = Vertex("2600 Taylorsville Blvd")
        vertex_l = Vertex("2835 Main St")
        vertex_m = Vertex("300 State St")
        vertex_n = Vertex("3060 Lester St")
        vertex_o = Vertex("3148 S 1100 W")
        vertex_p = Vertex("3365 S 900 W")
        vertex_q = Vertex("3575 W Valley Central Station bus Loop")
        vertex_r = Vertex("3595 Main St")
        vertex_s = Vertex("380 W 2880 S")
        vertex_t = Vertex("410 S State St")
        vertex_u = Vertex("4300 S 1300 E")
        vertex_v = Vertex("4580 S 2300 E")
        vertex_w = Vertex("5025 State St")
        vertex_x = Vertex("5100 South 2700 West")
        vertex_y = Vertex("5383 South 900 East #104")
        vertex_z = Vertex("600 E 900 South")

        #add vertexes to graph 
        g.add_vertex(vertex_hub)
        g.add_vertex(vertex_a)
        g.add_vertex(vertex_b)
        g.add_vertex(vertex_c)
        g.add_vertex(vertex_d)
        g.add_vertex(vertex_e)
        g.add_vertex(vertex_f)
        g.add_vertex(vertex_g)
        g.add_vertex(vertex_h)
        g.add_vertex(vertex_i)
        g.add_vertex(vertex_j)
        g.add_vertex(vertex_k)
        g.add_vertex(vertex_l)
        g.add_vertex(vertex_m)
        g.add_vertex(vertex_n)
        g.add_vertex(vertex_o)
        g.add_vertex(vertex_p)
        g.add_vertex(vertex_q)
        g.add_vertex(vertex_r)
        g.add_vertex(vertex_s)
        g.add_vertex(vertex_t)
        g.add_vertex(vertex_u)
        g.add_vertex(vertex_v)
        g.add_vertex(vertex_w)
        g.add_vertex(vertex_x)
        g.add_vertex(vertex_y)
        g.add_vertex(vertex_z)
        #hub to next vertex
        g.add_undirected_edge(vertex_hub, vertex_a, 3.6)
        g.add_undirected_edge(vertex_hub, vertex_b, 7.2)
        g.add_undirected_edge(vertex_hub, vertex_c, 3.8)
        g.add_undirected_edge(vertex_hub, vertex_d, 11.0)
        g.add_undirected_edge(vertex_hub, vertex_e, 2.2)
        g.add_undirected_edge(vertex_hub, vertex_f, 3.5)
        g.add_undirected_edge(vertex_hub, vertex_g, 10.9)
        g.add_undirected_edge(vertex_hub, vertex_h, 8.6)
        g.add_undirected_edge(vertex_hub, vertex_i, 7.6)
        g.add_undirected_edge(vertex_hub, vertex_j, 2.8)
        g.add_undirected_edge(vertex_hub, vertex_k, 6.4)
        g.add_undirected_edge(vertex_hub, vertex_l, 3.2)
        g.add_undirected_edge(vertex_hub, vertex_m, 7.6)
        g.add_undirected_edge(vertex_hub, vertex_n, 5.2)
        g.add_undirected_edge(vertex_hub, vertex_o, 4.4)
        g.add_undirected_edge(vertex_hub, vertex_p, 3.7)
        g.add_undirected_edge(vertex_hub, vertex_q, 7.6)
        g.add_undirected_edge(vertex_hub, vertex_r, 2.0)
        g.add_undirected_edge(vertex_hub, vertex_s, 3.6)
        g.add_undirected_edge(vertex_hub, vertex_t, 6.5)
        g.add_undirected_edge(vertex_hub, vertex_u, 1.9)
        g.add_undirected_edge(vertex_hub, vertex_v, 3.4)
        g.add_undirected_edge(vertex_hub, vertex_w, 2.4)
        g.add_undirected_edge(vertex_hub, vertex_x, 6.4)
        g.add_undirected_edge(vertex_hub, vertex_y, 2.4)
        g.add_undirected_edge(vertex_hub, vertex_z, 5.0)
        #vertex_a to all other vertexes aside from hub which was already calculated
        g.add_undirected_edge(vertex_a, vertex_b, 13.0)
        g.add_undirected_edge(vertex_a, vertex_c, 7.4)
        g.add_undirected_edge(vertex_a, vertex_d, 10.1)
        g.add_undirected_edge(vertex_a, vertex_e, 5.5)
        g.add_undirected_edge(vertex_a, vertex_f, 7.2)
        g.add_undirected_edge(vertex_a, vertex_g, 14.2)
        g.add_undirected_edge(vertex_a, vertex_h, 10.7)
        g.add_undirected_edge(vertex_a, vertex_i, 14.1)
        g.add_undirected_edge(vertex_a, vertex_j, 6.0)
        g.add_undirected_edge(vertex_a, vertex_k, 6.8)
        g.add_undirected_edge(vertex_a, vertex_l, 6.4)
        g.add_undirected_edge(vertex_a, vertex_m, 14.1)
        g.add_undirected_edge(vertex_a, vertex_n, 10.5)
        g.add_undirected_edge(vertex_a, vertex_o, 8.8)
        g.add_undirected_edge(vertex_a, vertex_p, 8.4)
        g.add_undirected_edge(vertex_a, vertex_q, 13.6)
        g.add_undirected_edge(vertex_a, vertex_r, 5.2)
        g.add_undirected_edge(vertex_a, vertex_s, 6.9)
        g.add_undirected_edge(vertex_a, vertex_t, 13.1)
        g.add_undirected_edge(vertex_a, vertex_u, 4.1)
        g.add_undirected_edge(vertex_a, vertex_v, 4.7)
        g.add_undirected_edge(vertex_a, vertex_w, 3.1)
        g.add_undirected_edge(vertex_a, vertex_x, 7.8)
        g.add_undirected_edge(vertex_a, vertex_y, 1.3)
        g.add_undirected_edge(vertex_a, vertex_z, 8.3)
        #vertex z-b
        g.add_undirected_edge(vertex_z, vertex_b, 4.4)
        g.add_undirected_edge(vertex_z, vertex_c, 2.8)
        g.add_undirected_edge(vertex_z, vertex_d, 10.1)
        g.add_undirected_edge(vertex_z, vertex_e, 5.4)
        g.add_undirected_edge(vertex_z, vertex_f, 3.5)
        g.add_undirected_edge(vertex_z, vertex_g, 5.1)
        g.add_undirected_edge(vertex_z, vertex_h, 6.2)
        g.add_undirected_edge(vertex_z, vertex_i, 2.8)
        g.add_undirected_edge(vertex_z, vertex_j, 3.2)
        g.add_undirected_edge(vertex_z, vertex_k, 11.0)
        g.add_undirected_edge(vertex_z, vertex_l, 3.7)
        g.add_undirected_edge(vertex_z, vertex_m, 2.8)
        g.add_undirected_edge(vertex_z, vertex_n, 6.4)
        g.add_undirected_edge(vertex_z, vertex_o, 6.5)
        g.add_undirected_edge(vertex_z, vertex_p, 5.7)
        g.add_undirected_edge(vertex_z, vertex_q, 6.2)
        g.add_undirected_edge(vertex_z, vertex_r, 5.1)
        g.add_undirected_edge(vertex_z, vertex_s, 4.3)
        g.add_undirected_edge(vertex_z, vertex_t, 1.8)
        g.add_undirected_edge(vertex_z, vertex_u, 6.0)
        g.add_undirected_edge(vertex_z, vertex_v, 7.9)
        g.add_undirected_edge(vertex_z, vertex_w, 6.8)
        g.add_undirected_edge(vertex_z, vertex_x, 10.6)
        g.add_undirected_edge(vertex_z, vertex_y, 7.0)
        #y-b
        g.add_undirected_edge(vertex_y, vertex_b, 10.0)
        g.add_undirected_edge(vertex_y, vertex_c, 6.1)
        g.add_undirected_edge(vertex_y, vertex_d, 6.4)
        g.add_undirected_edge(vertex_y, vertex_e, 4.2)
        g.add_undirected_edge(vertex_y, vertex_f, 5.9)
        g.add_undirected_edge(vertex_y, vertex_g, 11.7)
        g.add_undirected_edge(vertex_y, vertex_h, 9.5)
        g.add_undirected_edge(vertex_y, vertex_i, 9.5)
        g.add_undirected_edge(vertex_y, vertex_j, 4.8)
        g.add_undirected_edge(vertex_y, vertex_k, 4.9)
        g.add_undirected_edge(vertex_y, vertex_l, 5.2)
        g.add_undirected_edge(vertex_y, vertex_m, 9.5)
        g.add_undirected_edge(vertex_y, vertex_n, 7.2)
        g.add_undirected_edge(vertex_y, vertex_o, 6.3)
        g.add_undirected_edge(vertex_y, vertex_p, 5.9)
        g.add_undirected_edge(vertex_y, vertex_q, 11.1)
        g.add_undirected_edge(vertex_y, vertex_r, 4.0)
        g.add_undirected_edge(vertex_y, vertex_s, 5.6)
        g.add_undirected_edge(vertex_y, vertex_t, 8.5)
        g.add_undirected_edge(vertex_y, vertex_u, 2.8)
        g.add_undirected_edge(vertex_y, vertex_v, 3.4)
        g.add_undirected_edge(vertex_y, vertex_w, 1.7)
        g.add_undirected_edge(vertex_y, vertex_x, 5.4)
        #x-b
        g.add_undirected_edge(vertex_x, vertex_b, 6.9)
        g.add_undirected_edge(vertex_x, vertex_c, 9.7)
        g.add_undirected_edge(vertex_x, vertex_d, 0.6)
        g.add_undirected_edge(vertex_x, vertex_e, 6.0)
        g.add_undirected_edge(vertex_x, vertex_f, 9.0)
        g.add_undirected_edge(vertex_x, vertex_g, 8.2)
        g.add_undirected_edge(vertex_x, vertex_h, 4.2)
        g.add_undirected_edge(vertex_x, vertex_i, 11.5)
        g.add_undirected_edge(vertex_x, vertex_j, 7.8)
        g.add_undirected_edge(vertex_x, vertex_k, 0.4)
        g.add_undirected_edge(vertex_x, vertex_l, 6.9)
        g.add_undirected_edge(vertex_x, vertex_m, 11.5)
        g.add_undirected_edge(vertex_x, vertex_n, 4.4)
        g.add_undirected_edge(vertex_x, vertex_o, 4.8)
        g.add_undirected_edge(vertex_x, vertex_p, 5.6)
        g.add_undirected_edge(vertex_x, vertex_q, 7.5)
        g.add_undirected_edge(vertex_x, vertex_r, 5.5)
        g.add_undirected_edge(vertex_x, vertex_s, 6.5)
        g.add_undirected_edge(vertex_x, vertex_t, 11.4)
        g.add_undirected_edge(vertex_x, vertex_u, 6.4)
        g.add_undirected_edge(vertex_x, vertex_v, 7.9)
        g.add_undirected_edge(vertex_x, vertex_w, 4.5)
        #w-b
        g.add_undirected_edge(vertex_w, vertex_b, 8.3)
        g.add_undirected_edge(vertex_w, vertex_c, 6.1)
        g.add_undirected_edge(vertex_w, vertex_d, 4.7)
        g.add_undirected_edge(vertex_w, vertex_e, 2.5)
        g.add_undirected_edge(vertex_w, vertex_f, 4.2)
        g.add_undirected_edge(vertex_w, vertex_g, 10.0)
        g.add_undirected_edge(vertex_w, vertex_h, 7.8)
        g.add_undirected_edge(vertex_w, vertex_i, 7.8)
        g.add_undirected_edge(vertex_w, vertex_j, 4.3)
        g.add_undirected_edge(vertex_w, vertex_k, 4.1)
        g.add_undirected_edge(vertex_w, vertex_l, 3.4)
        g.add_undirected_edge(vertex_w, vertex_m, 7.8)
        g.add_undirected_edge(vertex_w, vertex_n, 5.5)
        g.add_undirected_edge(vertex_w, vertex_o, 4.6)
        g.add_undirected_edge(vertex_w, vertex_p, 4.2)
        g.add_undirected_edge(vertex_w, vertex_q, 9.4)
        g.add_undirected_edge(vertex_w, vertex_r, 2.3)
        g.add_undirected_edge(vertex_w, vertex_s, 3.9)
        g.add_undirected_edge(vertex_w, vertex_t, 6.8)
        g.add_undirected_edge(vertex_w, vertex_u, 2.9)
        g.add_undirected_edge(vertex_w, vertex_v, 4.4)
        #v-b
        g.add_undirected_edge(vertex_v, vertex_b, 10.9)
        g.add_undirected_edge(vertex_v, vertex_c, 5.0)
        g.add_undirected_edge(vertex_v, vertex_d, 7.4)
        g.add_undirected_edge(vertex_v, vertex_e, 5.2)
        g.add_undirected_edge(vertex_v, vertex_f, 6.9)
        g.add_undirected_edge(vertex_v, vertex_g, 12.7)
        g.add_undirected_edge(vertex_v, vertex_h, 10.4)
        g.add_undirected_edge(vertex_v, vertex_i, 10.3)
        g.add_undirected_edge(vertex_v, vertex_j, 5.8)
        g.add_undirected_edge(vertex_v, vertex_k, 8.3)
        g.add_undirected_edge(vertex_v, vertex_l, 6.2)
        g.add_undirected_edge(vertex_v, vertex_m, 10.3)
        g.add_undirected_edge(vertex_v, vertex_n, 8.2)
        g.add_undirected_edge(vertex_v, vertex_o, 7.4)
        g.add_undirected_edge(vertex_v, vertex_p, 6.9)
        g.add_undirected_edge(vertex_v, vertex_q, 12.0)
        g.add_undirected_edge(vertex_v, vertex_r, 5.0)
        g.add_undirected_edge(vertex_v, vertex_s, 6.6)
        g.add_undirected_edge(vertex_v, vertex_t, 9.3)
        g.add_undirected_edge(vertex_v, vertex_u, 2.0)
        #u-b
        g.add_undirected_edge(vertex_u, vertex_b, 9.5)
        g.add_undirected_edge(vertex_u, vertex_c, 3.3)
        g.add_undirected_edge(vertex_u, vertex_d, 5.9)
        g.add_undirected_edge(vertex_u, vertex_e, 3.2)
        g.add_undirected_edge(vertex_u, vertex_f, 4.9)
        g.add_undirected_edge(vertex_u, vertex_g, 11.2)
        g.add_undirected_edge(vertex_u, vertex_h, 8.1)
        g.add_undirected_edge(vertex_u, vertex_i, 8.5)
        g.add_undirected_edge(vertex_u, vertex_j, 3.8)
        g.add_undirected_edge(vertex_u, vertex_k, 6.9)
        g.add_undirected_edge(vertex_u, vertex_l, 4.1)
        g.add_undirected_edge(vertex_u, vertex_m, 8.5)
        g.add_undirected_edge(vertex_u, vertex_n, 6.2)
        g.add_undirected_edge(vertex_u, vertex_o, 5.3)
        g.add_undirected_edge(vertex_u, vertex_p, 4.9)
        g.add_undirected_edge(vertex_u, vertex_q, 10.6)
        g.add_undirected_edge(vertex_u, vertex_r, 3.0)
        g.add_undirected_edge(vertex_u, vertex_s, 4.6)
        g.add_undirected_edge(vertex_u, vertex_t, 7.5)

        #t-b
        g.add_undirected_edge(vertex_t, vertex_b, 4.8)
        g.add_undirected_edge(vertex_t, vertex_c, 4.3)
        g.add_undirected_edge(vertex_t, vertex_d, 10.6)
        g.add_undirected_edge(vertex_t, vertex_e, 6.5)
        g.add_undirected_edge(vertex_t, vertex_f, 3.5)
        g.add_undirected_edge(vertex_t, vertex_g, 3.2)
        g.add_undirected_edge(vertex_t, vertex_h, 6.7)
        g.add_undirected_edge(vertex_t, vertex_i, 1.0)
        g.add_undirected_edge(vertex_t, vertex_j, 4.1)
        g.add_undirected_edge(vertex_t, vertex_k, 11.5)
        g.add_undirected_edge(vertex_t, vertex_l, 3.7)
        g.add_undirected_edge(vertex_t, vertex_m, 1.0)
        g.add_undirected_edge(vertex_t, vertex_n, 6.9)
        g.add_undirected_edge(vertex_t, vertex_o, 6.8)
        g.add_undirected_edge(vertex_t, vertex_p, 6.4)
        g.add_undirected_edge(vertex_t, vertex_q, 7.2)
        g.add_undirected_edge(vertex_t, vertex_r, 4.9)
        g.add_undirected_edge(vertex_t, vertex_s, 4.4)

        #s-b
        g.add_undirected_edge(vertex_s, vertex_b, 5.0)
        g.add_undirected_edge(vertex_s, vertex_c, 3.6)
        g.add_undirected_edge(vertex_s, vertex_d, 6.0)
        g.add_undirected_edge(vertex_s, vertex_e, 1.7)
        g.add_undirected_edge(vertex_s, vertex_f, 1.1)
        g.add_undirected_edge(vertex_s, vertex_g, 6.6)
        g.add_undirected_edge(vertex_s, vertex_h, 4.6)
        g.add_undirected_edge(vertex_s, vertex_i, 5.4)
        g.add_undirected_edge(vertex_s, vertex_j, 1.8)
        g.add_undirected_edge(vertex_s, vertex_k, 6.9)
        g.add_undirected_edge(vertex_s, vertex_l, 1.0)
        g.add_undirected_edge(vertex_s, vertex_m, 5.4)
        g.add_undirected_edge(vertex_s, vertex_n, 3.0)
        g.add_undirected_edge(vertex_s, vertex_o, 2.2)
        g.add_undirected_edge(vertex_s, vertex_p, 1.7)
        g.add_undirected_edge(vertex_s, vertex_q, 6.1)
        g.add_undirected_edge(vertex_s, vertex_r, 1.6)

        #r-b
        g.add_undirected_edge(vertex_r, vertex_b, 6.0)
        g.add_undirected_edge(vertex_r, vertex_c, 4.1)
        g.add_undirected_edge(vertex_r, vertex_d, 5.3)
        g.add_undirected_edge(vertex_r, vertex_e, 0.5)
        g.add_undirected_edge(vertex_r, vertex_f, 1.9)
        g.add_undirected_edge(vertex_r, vertex_g, 7.7)
        g.add_undirected_edge(vertex_r, vertex_h, 5.1)
        g.add_undirected_edge(vertex_r, vertex_i, 5.9)
        g.add_undirected_edge(vertex_r, vertex_j, 2.3)
        g.add_undirected_edge(vertex_r, vertex_k, 6.2)
        g.add_undirected_edge(vertex_r, vertex_l, 1.2)
        g.add_undirected_edge(vertex_r, vertex_m, 5.9)
        g.add_undirected_edge(vertex_r, vertex_n, 3.2)
        g.add_undirected_edge(vertex_r, vertex_o, 2.4)
        g.add_undirected_edge(vertex_r, vertex_p, 1.6)
        g.add_undirected_edge(vertex_r, vertex_q, 7.1)

        #q-b
        g.add_undirected_edge(vertex_q, vertex_b, 7.4)
        g.add_undirected_edge(vertex_q, vertex_c, 5.7)
        g.add_undirected_edge(vertex_q, vertex_d, 7.2)
        g.add_undirected_edge(vertex_q, vertex_e, 1.4)
        g.add_undirected_edge(vertex_q, vertex_f, 5.7)
        g.add_undirected_edge(vertex_q, vertex_g, 7.2)
        g.add_undirected_edge(vertex_q, vertex_h, 3.1)
        g.add_undirected_edge(vertex_q, vertex_i, 7.2)
        g.add_undirected_edge(vertex_q, vertex_j, 6.7)
        g.add_undirected_edge(vertex_q, vertex_k, 8.1)
        g.add_undirected_edge(vertex_q, vertex_l, 6.3)
        g.add_undirected_edge(vertex_q, vertex_m, 7.2)
        g.add_undirected_edge(vertex_q, vertex_n, 4.0)
        g.add_undirected_edge(vertex_q, vertex_o, 6.4)
        g.add_undirected_edge(vertex_q, vertex_p, 5.6)

        #p-b
        g.add_undirected_edge(vertex_p, vertex_b, 4.5)
        g.add_undirected_edge(vertex_p, vertex_c, 5.8)
        g.add_undirected_edge(vertex_p, vertex_d, 4.4)
        g.add_undirected_edge(vertex_p, vertex_e, 2.7)
        g.add_undirected_edge(vertex_p, vertex_f, 3.8)
        g.add_undirected_edge(vertex_p, vertex_g, 5.8)
        g.add_undirected_edge(vertex_p, vertex_h, 3.4)
        g.add_undirected_edge(vertex_p, vertex_i, 6.6)
        g.add_undirected_edge(vertex_p, vertex_j, 4.0)
        g.add_undirected_edge(vertex_p, vertex_k, 5.4)
        g.add_undirected_edge(vertex_p, vertex_l, 2.9)
        g.add_undirected_edge(vertex_p, vertex_m, 6.6)
        g.add_undirected_edge(vertex_p, vertex_n, 1.5)
        g.add_undirected_edge(vertex_p, vertex_o, 0.6)

        #o-b
        g.add_undirected_edge(vertex_o, vertex_b, 4.6)
        g.add_undirected_edge(vertex_o, vertex_c, 5.6)
        g.add_undirected_edge(vertex_o, vertex_d, 4.3)
        g.add_undirected_edge(vertex_o, vertex_e, 2.4)
        g.add_undirected_edge(vertex_o, vertex_f, 3.0)
        g.add_undirected_edge(vertex_o, vertex_g, 8.0)
        g.add_undirected_edge(vertex_o, vertex_h, 3.3)
        g.add_undirected_edge(vertex_o, vertex_i, 7.8)
        g.add_undirected_edge(vertex_o, vertex_j, 3.7)
        g.add_undirected_edge(vertex_o, vertex_k, 5.2)
        g.add_undirected_edge(vertex_o, vertex_l, 2.6)
        g.add_undirected_edge(vertex_o, vertex_m, 7.8)
        g.add_undirected_edge(vertex_o, vertex_n, 1.3)

        #n-b
        g.add_undirected_edge(vertex_n, vertex_b, 3.0)
        g.add_undirected_edge(vertex_n, vertex_c, 6.5)
        g.add_undirected_edge(vertex_n, vertex_d, 3.9)
        g.add_undirected_edge(vertex_n, vertex_e, 3.2)
        g.add_undirected_edge(vertex_n, vertex_f, 3.9)
        g.add_undirected_edge(vertex_n, vertex_g, 4.2)
        g.add_undirected_edge(vertex_n, vertex_h, 1.6)
        g.add_undirected_edge(vertex_n, vertex_i, 7.6)
        g.add_undirected_edge(vertex_n, vertex_j, 4.6)
        g.add_undirected_edge(vertex_n, vertex_k, 4.9)
        g.add_undirected_edge(vertex_n, vertex_l, 3.5)
        g.add_undirected_edge(vertex_n, vertex_m, 7.3)

        #m-b
        g.add_undirected_edge(vertex_m, vertex_b, 4.8)
        g.add_undirected_edge(vertex_m, vertex_c, 5.3)
        g.add_undirected_edge(vertex_m, vertex_d, 11.1)
        g.add_undirected_edge(vertex_m, vertex_e, 7.5)
        g.add_undirected_edge(vertex_m, vertex_f, 4.5)
        g.add_undirected_edge(vertex_m, vertex_g, 4.2)
        g.add_undirected_edge(vertex_m, vertex_h, 7.7)
        g.add_undirected_edge(vertex_m, vertex_i, 0.6)
        g.add_undirected_edge(vertex_m, vertex_j, 5.1)
        g.add_undirected_edge(vertex_m, vertex_k, 12.0)
        g.add_undirected_edge(vertex_m, vertex_l, 4.7)

        #l-b
        g.add_undirected_edge(vertex_l, vertex_b, 5.3)
        g.add_undirected_edge(vertex_l, vertex_c, 3.0)
        g.add_undirected_edge(vertex_l, vertex_d, 6.4)
        g.add_undirected_edge(vertex_l, vertex_e, 1.5)
        g.add_undirected_edge(vertex_l, vertex_f, 0.8)
        g.add_undirected_edge(vertex_l, vertex_g, 6.9)
        g.add_undirected_edge(vertex_l, vertex_h, 4.8)
        g.add_undirected_edge(vertex_l, vertex_i, 4.7)
        g.add_undirected_edge(vertex_l, vertex_j, 1.1)
        g.add_undirected_edge(vertex_l, vertex_k, 7.3)

        #k-b
        g.add_undirected_edge(vertex_k, vertex_b, 7.3)
        g.add_undirected_edge(vertex_k, vertex_c, 10.4)
        g.add_undirected_edge(vertex_k, vertex_d, 1.0)
        g.add_undirected_edge(vertex_k, vertex_e, 6.5)
        g.add_undirected_edge(vertex_k, vertex_f, 8.7)
        g.add_undirected_edge(vertex_k, vertex_g, 8.6)
        g.add_undirected_edge(vertex_k, vertex_h, 4.6)
        g.add_undirected_edge(vertex_k, vertex_i, 11.9)
        g.add_undirected_edge(vertex_k, vertex_j, 9.4)

        #j-b
        g.add_undirected_edge(vertex_j, vertex_b, 6.3)
        g.add_undirected_edge(vertex_j, vertex_c, 1.6)
        g.add_undirected_edge(vertex_j, vertex_d, 7.3)
        g.add_undirected_edge(vertex_j, vertex_e, 2.6)
        g.add_undirected_edge(vertex_j, vertex_f, 1.5)
        g.add_undirected_edge(vertex_j, vertex_g, 8.0)
        g.add_undirected_edge(vertex_j, vertex_h, 9.3)
        g.add_undirected_edge(vertex_j, vertex_i, 4.8)

        #i-b
        g.add_undirected_edge(vertex_i, vertex_b, 4.8)
        g.add_undirected_edge(vertex_i, vertex_c, 5.3)
        g.add_undirected_edge(vertex_i, vertex_d, 11.1)
        g.add_undirected_edge(vertex_i, vertex_e, 7.5)
        g.add_undirected_edge(vertex_i, vertex_f, 4.5)
        g.add_undirected_edge(vertex_i, vertex_g, 4.2)
        g.add_undirected_edge(vertex_i, vertex_h, 7.7)

        #h-b
        g.add_undirected_edge(vertex_h, vertex_b, 2.8)
        g.add_undirected_edge(vertex_h, vertex_c, 6.3)
        g.add_undirected_edge(vertex_h, vertex_d, 4.0)
        g.add_undirected_edge(vertex_h, vertex_e, 5.1)
        g.add_undirected_edge(vertex_h, vertex_f, 4.3)
        g.add_undirected_edge(vertex_h, vertex_g, 4.0)

        #g-b
        g.add_undirected_edge(vertex_g, vertex_b, 1.6)
        g.add_undirected_edge(vertex_g, vertex_c, 8.6)
        g.add_undirected_edge(vertex_g, vertex_d, 8.6)
        g.add_undirected_edge(vertex_g, vertex_e, 7.9)
        g.add_undirected_edge(vertex_g, vertex_f, 6.3)

        #f-b
        g.add_undirected_edge(vertex_f, vertex_b, 4.8)
        g.add_undirected_edge(vertex_f, vertex_c, 2.8)
        g.add_undirected_edge(vertex_f, vertex_d, 6.9)
        g.add_undirected_edge(vertex_f, vertex_e, 1.9)

        #e-b
        g.add_undirected_edge(vertex_e, vertex_b, 6.0)
        g.add_undirected_edge(vertex_e, vertex_c, 4.4)
        g.add_undirected_edge(vertex_e, vertex_d, 5.6)

        #d-b
        g.add_undirected_edge(vertex_d, vertex_b, 6.4)
        g.add_undirected_edge(vertex_d, vertex_c, 9.2)

        #c-b
        g.add_undirected_edge(vertex_c, vertex_b, 7.1)

        return g

    