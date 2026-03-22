import graphviz

# --- 0. Simple Web Stack ---
d0 = graphviz.Digraph('simple_web_stack', format='png')
d0.attr(rankdir='LR')
d0.node('user', 'User', shape='ellipse')
d0.node('server', 'Server (8.8.8.8)\n\n- Web Server (Nginx)\n- App Server\n- Codebase\n- Database (MySQL)', shape='box')
d0.edge('user', 'server', label='www.foobar.com\nHTTP')
d0.render('0-simple_web_stack')

# --- 1. Distributed Web Infrastructure ---
d1 = graphviz.Digraph('distributed_web', format='png')
d1.attr(rankdir='TB')
d1.node('user', 'User', shape='ellipse')
d1.node('lb', 'Load Balancer (HAproxy)', shape='box')
d1.node('s1', 'Server 1\n- Nginx\n- App Server\n- Codebase\n- MySQL (Primary)', shape='box')
d1.node('s2', 'Server 2\n- Nginx\n- App Server\n- Codebase\n- MySQL (Replica)', shape='box')

d1.edge('user', 'lb', label='www.foobar.com')
d1.edge('lb', 's1', label='Active')
d1.edge('lb', 's2', label='Active / Passive')
d1.render('1-distributed_web_infrastructure')

# --- 2. Secured and Monitored Web Infrastructure ---
d2 = graphviz.Digraph('secured_monitored', format='png')
d2.attr(rankdir='TB')
d2.node('user', 'User', shape='ellipse')
d2.node('fw_lb', 'Firewall 1', shape='box')
d2.node('lb', 'Load Balancer (HAproxy)\n+ SSL Certificate\n+ Monitoring Client', shape='box')

d2.node('s1', 'Firewall 2 + Server 1\n- Nginx, App, Code\n- MySQL (Primary)\n+ Monitoring Client', shape='box')
d2.node('s2', 'Firewall 3 + Server 2\n- Nginx, App, Code\n- MySQL (Replica)\n+ Monitoring Client', shape='box')
d2.node('monitor', 'Monitoring Service\n(e.g., SumoLogic)', shape='ellipse', style='filled', fillcolor='lightgrey')

d2.edge('user', 'fw_lb', label='HTTPS')
d2.edge('fw_lb', 'lb')
d2.edge('lb', 's1')
d2.edge('lb', 's2')
d2.edge('lb', 'monitor', style='dashed')
d2.edge('s1', 'monitor', style='dashed')
d2.edge('s2', 'monitor', style='dashed')
d2.render('2-secured_and_monitored_web_infrastructure')

# --- 3. Scale Up ---
d3 = graphviz.Digraph('scale_up', format='png')
d3.attr(rankdir='TB')
d3.node('user', 'User', shape='ellipse')

with d3.subgraph(name='cluster_lb') as c_lb:
    c_lb.attr(label='Load Balancer Cluster')
    c_lb.node('lb1', 'HAproxy 1', shape='box')
    c_lb.node('lb2', 'HAproxy 2', shape='box')
    
with d3.subgraph(name='cluster_web') as c_web:
    c_web.attr(label='Web Servers')
    c_web.node('web1', 'Nginx 1', shape='box')
    c_web.node('web2', 'Nginx 2', shape='box')

with d3.subgraph(name='cluster_app') as c_app:
    c_app.attr(label='Application Servers')
    c_app.node('app1', 'App Server 1', shape='box')
    c_app.node('app2', 'App Server 2', shape='box')

with d3.subgraph(name='cluster_db') as c_db:
    c_db.attr(label='Database Servers')
    c_db.node('db1', 'MySQL (Primary)', shape='box')
    c_db.node('db2', 'MySQL (Replica)', shape='box')

d3.edge('user', 'lb1')
d3.edge('user', 'lb2')

d3.edge('lb1', 'web1')
d3.edge('lb1', 'web2')
d3.edge('lb2', 'web1')
d3.edge('lb2', 'web2')

d3.edge('web1', 'app1')
d3.edge('web1', 'app2')
d3.edge('web2', 'app1')
d3.edge('web2', 'app2')

d3.edge('app1', 'db1')
d3.edge('app2', 'db1')

d3.edge('db1', 'db2', label='Replication', style='dashed')
d3.render('3-scale_up')

print("Bütün sxemlər yaradıldı!")
