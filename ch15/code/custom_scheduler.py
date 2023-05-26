from kubernetes import client, config, watch


def schedule_pod(cli, name):
    target = client.V1ObjectReference()
    target.kind = 'Node'
    target.apiVersion = 'v1'
    target.name = 'k3d-k3s-default-agent-0'
    meta = client.V1ObjectMeta()
    meta.name = name
    body = client.V1Binding(metadata=meta, target=target)
    print('Scheduling pod:', name)
    cli.api_client.configuration.client_side_validation = False

    # There is an open bug (https://github.com/kubernetes-client/python/issues/1616)
    # that causes this to raise an exception even after the operation succeeds
    # to workaround it just silently catcg the exception
    try:
        cli.create_namespaced_binding('default', body)
    except:
        pass


def main():
    config.load_kube_config()
    cli = client.CoreV1Api()
    print('Waiting for pending pods...')
    w = watch.Watch()
    for event in w.stream(cli.list_namespaced_pod, 'default'):
        o = event['object']
        if event['type'] != 'ADDED' or o.status.phase != 'Pending' or o.spec.scheduler_name != 'custom-scheduler':
            continue

        schedule_pod(cli, o.metadata.name)


if __name__ == '__main__':
    main()
